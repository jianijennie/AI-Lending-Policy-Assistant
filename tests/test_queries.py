import os
import sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import openpyxl
from src.query import query_policies
from src.config import QUESTION_BANK_PATH

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

def run_tests(max_questions=None):
    print("=" * 70)
    print("RETRIEVAL ACCURACY TEST SUITE")
    print("Project CMAP 2026 — Group 2")
    print("=" * 70)

    questions = load_questions()
    if max_questions:
        questions = questions[:max_questions]

    scores = []
    source_hits = 0
    by_lender = {}
    by_category = {}

    for i, test in enumerate(questions):
        print(f"\nTest {i+1}/{len(questions)} [{test['id']}] "
              f"{test['lender']} | {test['category']} | {test['difficulty']}")
        print(f"Q: {test['question']}")

        try:
            answer, nodes = query_policies(test["question"])
            time.sleep(1)
            score = score_answer(
                answer,
                test["gold_answer"],
                test["source_chunk_id"],
                nodes
            )

            retrieved_chunks = [n.metadata.get('chunk_id', '') for n in nodes]
            correct_source = test["source_chunk_id"] in retrieved_chunks

            if correct_source:
                source_hits += 1

            scores.append(score)

            # Track by lender
            lender = test["lender"]
            if lender not in by_lender:
                by_lender[lender] = []
            by_lender[lender].append(score)

            # Track by category
            cat = test["category"]
            if cat not in by_category:
                by_category[cat] = []
            by_category[cat].append(score)

            print(f"Source hit: {'PASS' if correct_source else 'FAIL'} "
                  f"(expected: {test['source_chunk_id']})")

        except Exception as e:
            print(f"ERROR: {e}")
            scores.append(1)

        print("-" * 70)

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