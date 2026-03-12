# Fault-Tolerant REST API Scraper

A Python script for automated data extraction from APIs using offset pagination. It collects datasets (e.g., product catalogs) and exports clean data to CSV. Ready for business integration.

## Key Features
- **Pagination Handling:** Automatic `skip` and `limit` shifting until the API is exhausted.
- **Fault Tolerance (Retries):** The script doesn't crash on HTTP server errors (500, 502, 503, 504). It pauses and retries the request.
- **Session Reuse:** Uses `requests.Session()` to reuse TCP connections, making requests significantly faster.
- **Basic Anti-Ban:** Spoofs headers (`User-Agent`, `Accept`) to bypass default bot protections.
- **Data Structuring:** Dumps parsed data directly into a `.csv` file via `pandas` with proper UTF-8 encoding.

## Tech Stack
- Python 3
- requests
- pandas

## Installation & Usage

1. Create and activate a virtual environment:
python3 -m venv .venv
source .venv/bin/activate

2. Install dependencies:
pip install -r requirements.txt

3. Run the scraper:
python main.py

## Output
The script generates a `products.csv` file in the project root containing the cleaned dataset (ID, Title, Price, Stock). Progress logs are printed to the console for monitoring.
