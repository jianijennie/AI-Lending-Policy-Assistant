import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import openpyxl
from src.query import query_policies
from src.config import QUESTION_BANK_PATH

MAX_WORKERS = 4

def load_questions():
    wb = openpyxl.load_workbook(QUESTION_BANK_PATH)
    ws = wb["QuestionBank"]
    questions = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        if row[0] and row[4]:  # must have ID and question
            questions.append({
                "id": row[0],
                "lender": row[1],
                "category": row[2],
                "difficulty": row[3],
                "question": row[4],
                "gold_answer": row[5],
                "source_chunk_id": row[6]
            })
    return questions

def score_answer(answer: str, gold_answer: str, source_chunk_id: str, nodes):
    answer_lower = answer.lower()
    gold_lower = gold_answer.lower()

    # Extract key numbers and terms from gold answer
    import re
    gold_numbers = re.findall(r'\d+\.?\d*%?', gold_lower)
    gold_numbers += re.findall(r'\$[\d,]+k?', gold_lower)

    numbers_found = sum(1 for n in gold_numbers if n in answer_lower)
    number_score = numbers_found / len(gold_numbers) if gold_numbers else 1.0

    # Check if correct source chunk was retrieved
    retrieved_chunks = [n.metadata.get('chunk_id', '') for n in nodes]
    source_hit = source_chunk_id in retrieved_chunks

    # Simple keyword overlap
    gold_words = set(gold_lower.split())
    answer_words = set(answer_lower.split())
    overlap = len(gold_words & answer_words) / len(gold_words) if gold_words else 0

    # Score 1-4
    if source_hit and number_score >= 0.8 and overlap >= 0.3:
        return 4
    elif source_hit and number_score >= 0.5:
        return 3
    elif source_hit or number_score >= 0.5:
        return 2
    else:
        return 1

def _run_one(test):
    try:
        answer, nodes = query_policies(test["question"], verbose=False)
        score = score_answer(
            answer,
            test["gold_answer"],
            test["source_chunk_id"],
            nodes
        )
        retrieved_chunks = [n.metadata.get('chunk_id', '') for n in nodes]
        correct_source = test["source_chunk_id"] in retrieved_chunks
        return {"test": test, "score": score, "correct_source": correct_source,
                "answer": answer, "retrieved_chunks": retrieved_chunks, "error": None}
    except Exception as e:
        return {"test": test, "score": 1, "correct_source": False,
                "answer": None, "retrieved_chunks": [], "error": str(e)}

def run_tests(max_questions=None, max_workers=MAX_WORKERS):
    print("=" * 70)
    print("RETRIEVAL ACCURACY TEST SUITE")
    print("Project CMAP 2026 — Group 2")
    print("=" * 70)

    questions = load_questions()
    if max_questions:
        questions = questions[:max_questions]

    outcomes = [None] * len(questions)
    done = 0

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_idx = {executor.submit(_run_one, test): i for i, test in enumerate(questions)}
        for future in as_completed(future_to_idx):
            i = future_to_idx[future]
            result = future.result()
            outcomes[i] = result
            done += 1
            test = result["test"]
            status = "ERROR" if result["error"] else ("PASS" if result["correct_source"] else "FAIL")
            print(f"[{done}/{len(questions)}] [{test['id']}] {test['lender']} | "
                  f"{test['category']} | {test['difficulty']} | score={result['score']} | "
                  f"source={status}" + (f" | error={result['error']}" if result["error"] else ""),
                  flush=True)

    scores = []
    source_hits = 0
    by_lender = {}
    by_category = {}

    for result in outcomes:
        test = result["test"]
        scores.append(result["score"])
        if result["correct_source"]:
            source_hits += 1

        lender = test["lender"]
        by_lender.setdefault(lender, []).append(result["score"])

        cat = test["category"]
        by_category.setdefault(cat, []).append(result["score"])

    # Summary
    total = len(scores)
    avg_score = sum(scores) / total
    perfect = sum(1 for s in scores if s == 4)
    source_hit_rate = source_hits / total * 100

    print(f"\n{'=' * 70}")
    print(f"FINAL RESULTS")
    print(f"{'=' * 70}")
    print(f"Questions tested:     {total}")
    print(f"Average score:        {avg_score:.2f}/4")
    print(f"Perfect scores (4/4): {perfect}/{total} ({perfect/total*100:.0f}%)")
    print(f"Source hit rate:      {source_hit_rate:.0f}%")

    print(f"\nBy lender:")
    for lender, s in by_lender.items():
        print(f"  {lender}: avg {sum(s)/len(s):.2f}/4 ({len(s)} questions)")

    print(f"\nBy category:")
    for cat, s in sorted(by_category.items()):
        print(f"  {cat}: avg {sum(s)/len(s):.2f}/4 ({len(s)} questions)")

    print(f"{'=' * 70}")

if __name__ == "__main__":
    # Run first 10 questions to test, then remove the limit for full run
    run_tests(max_questions=None)