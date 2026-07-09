import os
import sys
import re
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from llama_index.core import VectorStoreIndex, StorageContext, Document
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
import chromadb
from src.config import CHUNKS_DIR, CHROMA_DIR, EMBEDDING_MODEL, CHUNK_SIZE, CHUNK_OVERLAP

def parse_chunk_file(filepath):
    """Parse a markdown chunk file into a list of Document objects."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Split into individual chunks on ## chunk_id:
    raw_chunks = re.split(r'\n---\n', content)
    documents = []

    for raw in raw_chunks:
        # Skip file header sections (no chunk_id)
        if '## chunk_id:' not in raw:
            continue

        # Extract chunk_id
        chunk_id_match = re.search(r'## chunk_id:\s*(\S+)', raw)
        if not chunk_id_match:
            continue
        chunk_id = chunk_id_match.group(1).strip()

        # Extract metadata fields
        def get_field(field_name):
            pattern = rf'\*\*{field_name}:\*\*\s*(.+?)(?:\n|$)'
            match = re.search(pattern, raw)
            return match.group(1).strip() if match else ""

        lenders = get_field("lenders")
        intent = get_field("intent")
        borrower_profile = get_field("borrower_profile")
        asset_class = get_field("asset_class")
        doc_type = get_field("doc_type")
        loan_size_band = get_field("loan_size_band")
        answerable_questions = get_field("answerable_questions")
        trigger_words = get_field("trigger_words")
        confidence = get_field("confidence")
        last_verified = get_field("last_verified")
        policy_fields = get_field("policy_fields")
        source = get_field("source")

        # Extract content (everything after **Content:**)
        content_match = re.search(r'\*\*Content:\*\*\s*\n(.*?)(?=\n---|\Z)', raw, re.DOTALL)
        if not content_match:
            continue
        chunk_content = content_match.group(1).strip()

        # Build enriched text for embedding
        # Prepend answerable_questions and trigger_words so the
        # embedding model learns to associate these terms with the chunk
        enriched_text = f"""Questions this chunk answers: {answerable_questions}
Key terms: {trigger_words}

{chunk_content}"""

        # Build metadata dict for ChromaDB filtering
        metadata = {
            "chunk_id": chunk_id,
            "lenders": lenders,
            "topic_intent": intent,
            "borrower_profile": borrower_profile,
            "asset_class": asset_class,
            "doc_type": doc_type,
            "loan_size_band": loan_size_band,
            "answerable_questions": answerable_questions,
            "confidence": confidence,
            "last_verified": last_verified,
            "policy_fields": policy_fields,
            "source": source,
            "file_name": os.path.basename(filepath)
        }

        documents.append(Document(
            text=enriched_text,
            metadata=metadata,
            id_=chunk_id
        ))

    return documents


def ingest_chunks():
    print("Parsing chunk files...")
    all_documents = []

    chunk_files = [f for f in os.listdir(CHUNKS_DIR) if f.endswith('.md')]
    for filename in sorted(chunk_files):
        filepath = os.path.join(CHUNKS_DIR, filename)
        docs = parse_chunk_file(filepath)
        print(f"  {filename}: {len(docs)} chunks parsed")
        all_documents.extend(docs)

    print(f"\nTotal chunks: {len(all_documents)}")

    print("\nSetting up embedding model...")
    embed_model = HuggingFaceEmbedding(model_name=EMBEDDING_MODEL)
    Settings.embed_model = embed_model
    Settings.llm = None

    print("Setting up ChromaDB...")
    chroma_client = chromadb.PersistentClient(path=CHROMA_DIR)

    # Delete and recreate the policy chunks collection
    try:
        chroma_client.delete_collection("lifex_policies")
        print("Deleted old collection")
    except:
        pass

    chroma_collection = chroma_client.get_or_create_collection("lifex_policies")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    print("Embedding and storing chunks...")
    splitter = SentenceSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    index = VectorStoreIndex.from_documents(
        all_documents,
        storage_context=storage_context,
        transformations=[splitter],
        show_progress=True
    )

    final_count = chroma_collection.count()
    print(f"\nDone. {final_count} chunks stored in ChromaDB.")

    # Verify a sample
    print("\nSample verification — checking metadata on first 3 stored chunks:")
    sample = chroma_collection.get(limit=3, include=["metadatas"])
    for i, meta in enumerate(sample["metadatas"]):
        print(f"  [{i+1}] chunk_id: {meta.get('chunk_id')} | "
              f"lender: {meta.get('lenders')} | "
              f"intent: {meta.get('topic_intent')}")

    return index


if __name__ == "__main__":
    ingest_chunks()