import requests
import pandas as pd
import time


def parse_dummyjson():
    base_url = "https://dummyjson.com/products"
    limit = 30
    skip = 0
    all_products = []

    print("start collecting data")

    while True:

        params = {
            "limit": limit,
            "skip": skip
        }

        response = requests.get(base_url, params=params, timeout=10)

        response.raise_for_status()
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

        print(f"Collected {len(all_products)} from {data.get('total', '???')} products ")

        skip += limit

        time.sleep(0.5)

    df = pd.DataFrame(all_products)
    df.to_csv("products.csv", index=False, encoding="utf-8")
    print(f"Done. The products.csv file has been saved. Total records: {len(df)}")


if __name__ == "__main__":
    parse_dummyjson()


