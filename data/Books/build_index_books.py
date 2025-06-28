import os
import json
import pickle
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))  # Adjust path to include backend and src directories
from src.embeddings import EmbeddingManager
from backend.config import Config

def load_books_data(book_path: str) -> dict:
    data = {}
    for file in os.listdir(book_path):
        if file.endswith(".json"):
            genre = file.replace(".json", "")
            with open(os.path.join(book_path, file), 'r', encoding='utf-8') as f:
                data[genre] = json.load(f)
    return data

if __name__ == "__main__":
    book_path = Config.BOOK_JSON_PATH
    output_path = Config.BOOK_EMBEDDING_PATH

    print("📚 Loading book data...")
    book_data = load_books_data(book_path)

    all_titles = []
    all_texts = []

    for genre, books in book_data.items():
        for title, summary in books.items():
            all_titles.append(f"{title} ({genre})")
            all_texts.append(summary)

    print(f"✅ Loaded {len(all_texts)} book summaries")

    print("🧠 Generating embeddings...")
    embedder = EmbeddingManager()
    embeddings = embedder.generate_embedding(all_texts)

    print(f"💾 Saving embeddings to {output_path}...")
    with open(output_path, 'wb') as f:
        pickle.dump({
            "titles": all_titles,
            "embeddings": embeddings
        }, f)

    print("🎉 Done! Embeddings saved.")
# This script builds an index of book summaries and generates embeddings for them.
# It loads book data from JSON files, generates embeddings using the EmbeddingManager,