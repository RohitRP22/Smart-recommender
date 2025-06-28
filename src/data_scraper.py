import wikipedia
import requests
def scrape_wikipedia_summary(title):
    import requests
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        description = data.get("description", "").lower()

        # Check if it's a movie or book
        if "film" in description or "movie" in description or "novel" in description or "book" in description:
            return data.get("extract")
        else:
            print(f"⚠️ Skipped: '{title}' is not a movie or book.")
            return None
    else:
        return None
