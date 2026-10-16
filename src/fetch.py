import requests
from datetime import datetime, timezone

from src.config import NBP_API_URL


def fetch_exchange_rates() -> list[dict]:
    """Pobiera aktualne kursy walut z API NBP i zwraca listę słowników,
    gotowych do wrzucenia do BigQuery."""

    response = requests.get(NBP_API_URL, timeout=10)
    response.raise_for_status()  # rzuci wyjątek jeśli status != 200

    data = response.json()
    table = data[0]  # API zwraca listę z jednym elementem (tabela A)

    fetched_at = datetime.now(timezone.utc).isoformat()
    effective_date = table["effectiveDate"]

    rows = []
    for rate in table["rates"]:
        rows.append({
            "currency_code": rate["code"],
            "currency_name": rate["currency"],
            "mid_rate": rate["mid"],
            "effective_date": effective_date,
            "fetched_at": fetched_at,
        })

    return rows