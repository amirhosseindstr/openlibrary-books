# OpenLibrary Books Fetcher

A small Python script that:

1. Fetches 50 books from the public [OpenLibrary](https://openlibrary.org/developers/api) search API
2. Keeps only books first published after the year 2000
3. Sorts them by publication year
4. Saves the result to `books.csv`

## Requirements

- Python 3.8+
- `requests`

## Usage

```bash
pip install -r requirements.txt
python fetch_books.py
```

The output file `books.csv` has the columns: `title`, `author`, `year`, `link`.

## Configuration

Change the search topic by editing the `query` argument of `fetch_books()` in `fetch_books.py`.

## Sample output

See `books.csv` in this repository.
