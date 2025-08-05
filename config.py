import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for the basketball analysis chatbot."""
    
    # Hugging Face Configuration
    HUGGINGFACE_API_TOKEN = os.getenv("")
    MODEL_NAME = os.getenv("MODEL_NAME", "meta-llama/Llama-3-7b-chat-hf")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    
    # Pinecone Configuration
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
    PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "basketball-analysis")
    
    # Model Parameters
    MAX_LENGTH = 2048
    TEMPERATURE = 0.7
    TOP_P = 0.9
    
    # Vector Database Parameters
    VECTOR_DIMENSION = 384
    METRIC = "cosine"
    
    # Basketball Analysis Parameters
    MAX_TOKENS = 1000
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200 