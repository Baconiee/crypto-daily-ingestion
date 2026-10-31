from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import psycopg
import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timezone
from psycopg.types.json import Jsonb
import json


load_dotenv()

retry = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[500, 502, 503, 504],
    allowed_methods=["GET"]
)

header = {
    "x-cg-demo-api-key": os.environ["API_KEY"]
} 

URL =  'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
session = requests.Session()
adapter = HTTPAdapter(max_retries=retry)
session.mount("https://", adapter)

def extract_crypto_data():
    response = session.get(URL, headers=header, timeout=10)
    extracted_at = datetime.now(timezone.utc)
    response.raise_for_status()
    crypto_data = response.json()

    return crypto_data, extracted_at

