import json
import os

DATA_PATH = "D:\Projects\movie_recommender\data\knowledge_store.json"

def load_data() -> dict:
    if not os.path.exists(DATA_PATH):
        return {}
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        content = f.read().strip()
        if not content:
            return {}
        return json.loads(content)

def save_data(data: dict) -> None:
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_entry(topic: str) -> str:
    data = load_data()
    return data.get(topic.lower(), "")

def add_entry(topic: str, summary: str) -> None:
    data = load_data()
    data[topic.lower()] = summary
    save_data(data)
