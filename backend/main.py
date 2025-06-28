from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import os
import sys

# Add parent directory to sys.path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_scraper import scrape_wikipedia_summary
from src.utils.json_store import get_entry, add_entry

app = FastAPI(title="Wikipedia Summary API")

class SummaryResponse(BaseModel):
    topic: str
    summary: str

@app.get("/summary", response_model=SummaryResponse)
def get_summary_api(topic: str = Query(..., description="Topic to search on Wikipedia")):
    summary = get_entry(topic)
    if summary:
        return SummaryResponse(topic=topic, summary=summary)

    summary = scrape_wikipedia_summary(topic)
    if summary:
        add_entry(topic, summary)
        return SummaryResponse(topic=topic, summary=summary)
    
    raise HTTPException(status_code=404, detail="No information found for this topic.")

# Optional root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome! Use /summary?topic=YourTopic to get a Wikipedia summary."}
