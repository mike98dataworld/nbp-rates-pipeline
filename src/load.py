import pandas as pd
from google.cloud import bigquery

from src.config import PROJECT_ID, TABLE_ID


def load_to_bigquery(rows: list[dict]) -> None:
    """Zapisuje listę słowników jako nowe wiersze w tabeli BigQuery."""

    if not rows:
        print("Brak danych do zapisania - pomijam.")
        return

    df = pd.DataFrame(rows)

    client = bigquery.Client(project=PROJECT_ID)

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_APPEND",  # dopisuj, nie nadpisuj tabeli
    )

    job = client.load_table_from_dataframe(
        df, TABLE_ID, job_config=job_config
    )
    job.result()  # czeka aż operacja się zakończy

    print(f"Zapisano {len(df)} wierszy do {TABLE_ID}")