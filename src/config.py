import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env'))

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DATA_DIR = "C:/Projects/lifex-python/data/documents"
CHROMA_DIR = "C:/Projects/chroma_db"

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
LLM_MODEL = "llama-3.1-8b-instant"

CHUNKS_DIR = "C:/Projects/lifex-python/data/chunks"
METADATA_PATH = "C:/Projects/lifex-python/data/metadata/Metadata.csv"
QUESTION_BANK_PATH = "C:/Projects/lifex-python/data/metadata/QuestionBank.xlsx"
GROUND_TRUTH_PATH = "C:/Projects/lifex-python/data/metadata/GroundTruth.xlsx"

CHUNK_SIZE = 1024
CHUNK_OVERLAP = 50
TOP_K = 5