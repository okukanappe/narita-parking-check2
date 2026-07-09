import os
import re
import requests

URL = "https://parking.narita-airport.jp/ja/reservation/calendar-p2s"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "ja,en;q=0.9",
}

response = requests.get(
    URL,
    headers=headers,
    timeout=30,
)

response.raise_for_status()
