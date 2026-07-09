import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
import chromadb
from src.config import DATA_DIR, CHROMA_DIR, CHUNK_SIZE, CHUNK_OVERLAP, EMBEDDING_MODEL

def ingest_documents():
    print("Loading documents...")
    documents = SimpleDirectoryReader(
        DATA_DIR,
        recursive=True,
        required_exts=[".pdf"]
    ).load_data()

    print(f"Loaded {len(documents)} document pages")

    print("Setting up embedding model...")
    embed_model = HuggingFaceEmbedding(model_name=EMBEDDING_MODEL)
    Settings.embed_model = embed_model
    Settings.llm = None

    print("Setting up ChromaDB...")
    chroma_client = chromadb.PersistentClient(path=CHROMA_DIR)
    chroma_collection = chroma_client.get_or_create_collection("lifex_policies")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    print("Chunking and embedding documents...")
    splitter = SentenceSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context,
        transformations=[splitter],
        show_progress=True
    )

    print("Done. Documents ingested into ChromaDB.")
    return index

if __name__ == "__main__":
    ingest_documents()