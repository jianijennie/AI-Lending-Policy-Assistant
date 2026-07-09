import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DATA_DIR = "data/documents"
CHROMA_DIR = "chroma_db"

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
LLM_MODEL = "llama-3.3-70b-versatile"

CHUNK_SIZE = 512
CHUNK_OVERLAP = 50
TOP_K = 5