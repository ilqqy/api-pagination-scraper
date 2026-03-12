import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import pandas as pd
import time


def get_session():
    session = requests.Session()

    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json"
    })

    retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    return session


def parse_dummyjson():
    base_url = "https://dummyjson.com/products"
    limit = 30
    skip = 0
    all_products = []

    session = get_session()
    print("Start collecting data... ")

    while True:
        params = {"limit": limit, "skip": skip}

        try:
            response = session.get(base_url, params=params, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f" connection error on skip={skip}: {e}")

        data = response.json()
        products = data.get("products", [])

        if not products:
            break

        for item in products:
            all_products.append({
                "id": item.get("id"),
                "title": item.get("title"),
                "price": item.get("price"),
                "stock": item.get("stock")
            })

        print(f"Collected {len(all_products)} from {data.get('total')} products...")
        skip += limit
        time.sleep(0.5)

    if all_products:
        df = pd.DataFrame(all_products)
        df.to_csv("products.csv", index=False, encoding="utf-8")
        print(f"Done. Saved products.csv. Records: {len(df)}")
    else:
        print("Data not collected, CSV not created.")


if __name__ == "__main__":
    parse_dummyjson()
