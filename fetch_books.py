import csv
import sys
import requests

API_URL = "https://openlibrary.org/search.json"
OUTPUT_FILE = "books.csv"
BOOK_COUNT = 50
MIN_YEAR = 2000

def fetch_books(query="programming", limit=BOOK_COUNT):
    """Return a list of raw book records from the OpenLibrary search API."""
    params = {
        "q": query,
        "limit": limit,
        "fields": "title,author_name,first_publish_year,key",
    }
    response = requests.get(API_URL, params=params, timeout=30)
    response.raise_for_status()
    return response.json().get("docs", [])

def clean_and_filter(docs, min_year=MIN_YEAR):
    """Keep only books published after min_year and normalize the fields."""
    books = []
    for doc in docs:
        year = doc.get("first_publish_year")
        if year is None or year <= min_year:
            continue
        books.append(
            {
                "title": doc.get("title", "Unknown"),
                "author": ", ".join(doc.get("author_name", ["Unknown"])),
                "year": year,
                "link": "https://openlibrary.org" + doc.get("key", ""),
            }
        )
    return sorted(books, key=lambda b: b["year"])

def save_csv(books, path=OUTPUT_FILE):
    """Write the books to a CSV file."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "author", "year", "link"])
        writer.writeheader()
        writer.writerows(books)

def main():
    try:
        docs = fetch_books()
    except requests.RequestException as error:
        print(f"Failed to fetch data: {error}", file=sys.stderr)
        sys.exit(1)

    books = clean_and_filter(docs)
    save_csv(books)
    print(f"Fetched {len(docs)} books, saved {len(books)} (after {MIN_YEAR}) to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
