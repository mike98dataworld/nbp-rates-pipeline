import os
from dotenv import load_dotenv

# Wczytuje zmienne z pliku .env do środowiska
load_dotenv()

PROJECT_ID = os.getenv("GCP_PROJECT_ID")
DATASET = os.getenv("BQ_DATASET")
TABLE_NAME = "exchange_rates"

# Pełna nazwa tabeli w formacie wymaganym przez BigQuery
TABLE_ID = f"{PROJECT_ID}.{DATASET}.{TABLE_NAME}"

NBP_API_URL = "http://api.nbp.pl/api/exchangerates/tables/A/?format=json"