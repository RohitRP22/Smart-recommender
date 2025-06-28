import os
import sys
import json
import pickle
from typing import Dict, List
from google.generativeai import embed_content  # Gemini embeddings
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.config import Config
# future use.

class EmbeddingManager:
    def __init__(self):
        self.api_key = Config.GOOGLE_API_KEY
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY is missing in Config.")
    
        self.api_key = Config.GOOGLE_API_KEY
        os.environ["GOOGLE_API_KEY"] = self.api_key
        self.model = Config.EMBEDDING_MODEL

    def load_json_data(self, file_path: str) -> Dict[str, str]:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def save_embeddings(self, embeddings: List[List[float]], titles: List[str], path: str):
        with open(path, 'wb') as f:
            pickle.dump({"titles": titles, "embeddings": embeddings}, f)
        print(f"✅ Embeddings saved at {path}")

    def generate_embedding(self, text: str) -> List[float]:
        response = embed_content(
            model=self.model,
            content=text,
            task_type="retrieval_document"
        )
        return response["embedding"]

    def process_json_file(self, json_path: str, output_pkl_path: str):
        data = self.load_json_data(json_path)
        embeddings = []
        titles = []

        for title, summary in data.items():
            if summary:
                print(f"🔍 Embedding for: {title}")
                emb = self.generate_embedding(summary)
                embeddings.append(emb)
                titles.append(title)

        self.save_embeddings(embeddings, titles, output_pkl_path)
