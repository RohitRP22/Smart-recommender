# movie_recommender/data/scrapper.py
# This module provides functionality to scrape Wikipedia for movie summaries.
from dotenv import load_dotenv
import os
import wikipediaapi

# Load environment variables from .env file
load_dotenv()
user_agent = os.getenv("WIKI_USER_AGENT")

class WikipediaScraper:
    def __init__(self, language='en'):
        self.wiki = wikipediaapi.Wikipedia(user_agent=user_agent, language='en')
        if not self.wiki:
            raise ValueError("Failed to initialize Wikipedia API. Check your user agent and network connection.")

    def fetch_summary(self, title: str, max_chars: int = 1000) -> str:
        page = self.wiki.page(title)
        if page.exists():
            return page.summary[:max_chars]
        return "Summary not found."

    def fetch_multiple_summaries(self, titles: list, max_chars: int = 1000) -> dict:
        data = {}
        for title in titles:
            data[title] = self.fetch_summary(title, max_chars)
        return data
