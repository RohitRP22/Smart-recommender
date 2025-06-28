import os
import sys
from dotenv import load_dotenv
from pathlib import Path
import google.generativeai as genai
sys.path.append(str(Path(__file__).resolve().parent.parent.parent)) 
# Load .env file
load_dotenv()
# Configure Google Generative AI API
# Ensure you have the GOOGLE_API_KEY set in your .env file



class Config:
    # 🔐 API Keys
    GOOGLE_API_KEY = genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  # Replace with your actual API key

    # 🤖 Model Info
    EMBEDDING_MODEL = "models/embedding-001"

    # 📁 Paths
    BOOK_JSON_PATH = "D:\Projects\movie_recommender\data\Books"  # Adjust this path as needed
    MOVIE_JSON_PATH = "D:\Projects\movie_recommender\data\Movie" 
    BOOK_EMBEDDING_PATH = "data/embeddings/book_embeddings.pkl"
    MOVIE_EMBEDDING_PATH = "data/embeddings/movie_embeddings.pkl"
