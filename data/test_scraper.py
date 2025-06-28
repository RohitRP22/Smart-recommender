from movie_recommender.data.Movie_Scraper import WikipediaScraper
from movie_recommender.data.Books_Scraper import BookScraper

# if __name__ == "__main__":
#     scraper = WikipediaScraper()
#     titles = ["Inception", "The Matrix", "Interstellar"]
#     summaries = scraper.fetch_multiple_summaries(titles)
    
#     for title, summary in summaries.items():
#         print(f"\n📘 {title}:\n{summary[:300]}...\n")
        

if __name__ == "__main__":
    scraper = BookScraper()
    titles = ["To Kill a Mockingbird", "1984", "Pride and Prejudice"]
    summaries = scraper.fetch_multiple_summaries(titles)

    for title, summary in summaries.items():
        print(f"\n📚 {title}:\n{summary[:300]}...\n")
