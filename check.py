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

print("プログラム開始")

response = requests.get(
    URL,
    headers=headers,
    timeout=30,
)

print(f"HTTPステータス: {response.status_code}")

response.raise_for_status()

html = response.text

print(f"HTML取得: {len(html)}文字")

match = re.search(r'"P0814":"([BCN])"', html)

if match is None:
    print("P0814が見つかりませんでした")
    exit(1)

status = match.group(1)

print(f"P0814 = {status}")

if status == "B":
    print("空きあり！通知します")

    requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": os.environ["PUSHOVER_TOKEN"],
            "user": os.environ["PUSHOVER_USER"],
            "title": "成田空港P2",
            "message": "8/14 PM に空きが出ました！",
        },
    )
else:
    print("まだ空きなし")
