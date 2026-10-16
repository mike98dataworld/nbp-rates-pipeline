# NBP Rates Pipeline

Prosty pipeline danych: pobiera aktualne kursy walut z publicznego API NBP i zapisuje je do tabeli w Google BigQuery.

Projekt z serii portfolio, w której uczę się budować pipeline'y danych end-to-end (Python → BigQuery → dbt → Airflow).

## Jak to działa

1. `fetch.py` pobiera tabelę kursów A z API NBP i zamienia ją na płaską listę rekordów
2. `load.py` zapisuje rekordy do BigQuery (`WRITE_APPEND`, więc historia kursów się kumuluje)
3. `main.py` spina oba kroki w jedno uruchomienie

Każdy rekord zawiera: kod i nazwę waluty, kurs średni, datę obowiązywania kursu oraz timestamp pobrania (`fetched_at`).

## Stack

- Python 3.11
- `requests`, `pandas`
- Google BigQuery (`google-cloud-bigquery`)
- `python-dotenv` do konfiguracji

## Struktura projektu

```
nbp-rates-pipeline/
├── main.py            # punkt wejścia
├── src/
│   ├── config.py      # konfiguracja ze zmiennych środowiskowych
│   ├── fetch.py       # pobieranie danych z API NBP
│   └── load.py        # zapis do BigQuery
├── requirements.txt
└── .env               # lokalnie, poza gitem
```

## Uruchomienie

1. Utwórz środowisko i zainstaluj zależności:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Utwórz projekt GCP, dataset w BigQuery oraz service account z rolami `BigQuery Data Editor` i `BigQuery Job User`, a następnie pobierz klucz JSON.

3. Utwórz plik `.env` w głównym folderze:

```
GOOGLE_APPLICATION_CREDENTIALS=service-account-key.json
GCP_PROJECT_ID=<id-projektu-gcp>
BQ_DATASET=<nazwa-datasetu>
```

4. Uruchom:

```bash
python main.py
```

Plik `.env` i klucz JSON są w `.gitignore` i nigdy nie trafiają do repozytorium.

## Plan rozwoju

- [ ] Workflow Git (branche + Pull Requesty)
- [ ] Transformacje w dbt (warstwy staging i marts, testy)
- [ ] Orkiestracja w Airflow
- [ ] CI w GitHub Actions