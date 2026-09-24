# 📚 OpenLibrary Books Fetcher

**English** | [فارسی](#-فارسی)

A small, clean Python script that fetches book data from the public [OpenLibrary Search API](https://openlibrary.org/dev/docs/api/search), keeps only books first published **after the year 2000**, sorts them by year, and exports the result to a CSV file.

## Features

- Fetches 50 books from the OpenLibrary public API (no API key required)
- Filters out books published in 2000 or earlier, and books with no publication year
- Sorts the remaining books by publication year (oldest to newest)
- Saves the output to `books.csv` (UTF-8, opens fine in Excel / LibreOffice)
- Handles network errors gracefully with a clear message and a non-zero exit code
- Small, readable functions, each with a single responsibility

## Project Structure

```
openlibrary-books/
├── fetch_books.py     # main script
├── requirements.txt   # Python dependencies
├── books.csv          # generated output
├── README.md          # this file
└── .gitignore
```

## Requirements

- Python 3.8 or newer
- [`requests`](https://pypi.org/project/requests/)

## Installation

```bash
git clone https://github.com/USERNAME/openlibrary-books.git
cd openlibrary-books

# (recommended) create a virtual environment
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

## Usage

```bash
python3 fetch_books.py
```

Example console output:

```
Fetched 50 books, saved 25 (after 2000) to books.csv
```

The number of saved books can be lower than 50, because books published in 2000 or earlier are filtered out.

## Output Format

`books.csv` has the following columns:

| Column   | Description                                   |
|----------|-----------------------------------------------|
| `title`  | Book title                                    |
| `author` | Author name(s), separated by commas           |
| `year`   | First publication year                        |
| `link`   | Link to the book page on openlibrary.org      |

## How It Works

1. `fetch_books()` sends a GET request to the OpenLibrary search endpoint and returns the raw list of books.
2. `clean_and_filter()` drops books with no year or published in 2000 or earlier, normalizes the fields, and sorts by year.
3. `save_csv()` writes the final list to `books.csv`.
4. `main()` runs these steps in order and handles network errors.

## Configuration

You can change the following values at the top of `fetch_books.py`:

| Constant       | Default     | Meaning                              |
|----------------|-------------|--------------------------------------|
| `BOOK_COUNT`   | `50`        | Number of books to fetch             |
| `MIN_YEAR`     | `2000`      | Keep only books published after this year |
| `OUTPUT_FILE`  | `books.csv` | Output file name                     |

To search a different topic, change the `query` argument in `fetch_books()` (default: `"programming"`).

## Error Handling

If the API is unreachable or returns an error, the script prints a message to stderr and exits with code `1`. Requests time out after 30 seconds.

---

# 🇮🇷 فارسی

یک اسکریپت پایتون ساده و تمیز که اطلاعات کتاب‌ها را از API عمومی [OpenLibrary](https://openlibrary.org/dev/docs/api/search) می‌گیرد، فقط کتاب‌هایی را نگه می‌دارد که **بعد از سال ۲۰۰۰** برای اولین بار منتشر شده‌اند، آن‌ها را بر اساس سال مرتب می‌کند و در یک فایل CSV ذخیره می‌کند.

## امکانات

- دریافت ۵۰ کتاب از API عمومی OpenLibrary (بدون نیاز به کلید API)
- حذف کتاب‌های سال ۲۰۰۰ و قدیمی‌تر و همچنین کتاب‌هایی که سال انتشار ندارند
- مرتب‌سازی کتاب‌های باقی‌مانده بر اساس سال انتشار (از قدیمی به جدید)
- ذخیره خروجی در `books.csv` با کدگذاری UTF-8 (قابل باز شدن در Excel و LibreOffice)
- مدیریت خطای شبکه با پیام واضح
- کد شامل تابع‌های کوچک و خوانا، که هر کدام یک کار مشخص انجام می‌دهد

## ساختار پروژه

```
openlibrary-books/
├── fetch_books.py     # اسکریپت اصلی
├── requirements.txt   # وابستگی‌های پایتون
├── books.csv          # خروجی تولیدشده
├── README.md          # همین فایل
└── .gitignore
```

## پیش‌نیازها

- پایتون نسخه ۳.۸ یا بالاتر
- کتابخانه [`requests`](https://pypi.org/project/requests/)

## نصب

```bash
git clone https://github.com/USERNAME/openlibrary-books.git
cd openlibrary-books

# (پیشنهادی) ساخت محیط مجازی
python3 -m venv .venv
source .venv/bin/activate      # ویندوز: .venv\Scripts\activate

pip install -r requirements.txt
```

## نحوه اجرا

```bash
python3 fetch_books.py
```

نمونه خروجی در ترمینال:

```
Fetched 50 books, saved 25 (after 2000) to books.csv
```

تعداد کتاب‌های ذخیره‌شده ممکن است کمتر از ۵۰ باشد، چون کتاب‌های سال ۲۰۰۰ و قدیمی‌تر فیلتر می‌شوند.

## فرمت خروجی

فایل `books.csv` این ستون‌ها را دارد:

| ستون     | توضیح                                        |
|----------|----------------------------------------------|
| `title`  | عنوان کتاب                                   |
| `author` | نام نویسنده یا نویسندگان (جداشده با ویرگول)  |
| `year`   | سال اولین انتشار                             |
| `link`   | لینک صفحه کتاب در openlibrary.org            |

## نحوه کار

1. تابع `fetch_books()` یک درخواست GET به OpenLibrary می‌فرستد و لیست خام کتاب‌ها را برمی‌گرداند.
2. تابع `clean_and_filter()` کتاب‌های بدون سال یا سال ۲۰۰۰ و قدیمی‌تر را حذف می‌کند، فیلدها را مرتب می‌کند و بر اساس سال مرتب‌سازی می‌کند.
3. تابع `save_csv()` لیست نهایی را در `books.csv` می‌نویسد.
4. تابع `main()` این مراحل را به ترتیب اجرا می‌کند و خطاهای شبکه را مدیریت می‌کند.

## تنظیمات

این مقادیر در ابتدای فایل `fetch_books.py` قابل تغییرند:

| ثابت           | مقدار پیش‌فرض | معنی                                      |
|----------------|---------------|-------------------------------------------|
| `BOOK_COUNT`   | `50`          | تعداد کتاب‌هایی که دریافت می‌شود           |
| `MIN_YEAR`     | `2000`        | فقط کتاب‌های بعد از این سال نگه داشته شوند |
| `OUTPUT_FILE`  | `books.csv`   | نام فایل خروجی                            |

برای جستجوی موضوع دیگر، آرگومان `query` را در تابع `fetch_books()` تغییر بده (پیش‌فرض: `"programming"`).

## مدیریت خطا

اگر API در دسترس نباشد یا خطا برگرداند، اسکریپت یک پیام در stderr چاپ می‌کند و با کد `1` بسته می‌شود. درخواست‌ها بعد از ۳۰ ثانیه timeout می‌شوند.
