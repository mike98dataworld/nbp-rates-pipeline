from src.fetch import fetch_exchange_rates
from src.load import load_to_bigquery


def main():
    print("Pobieram kursy walut z NBP...")
    rows = fetch_exchange_rates()
    print(f"Pobrano {len(rows)} kursów walut.")

    print("Zapisuję do BigQuery...")
    load_to_bigquery(rows)

    print("Gotowe ✅")


if __name__ == "__main__":
    main()