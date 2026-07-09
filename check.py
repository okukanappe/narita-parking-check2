import os
import re
import requests

URL = "https://parking.narita-airport.jp/ja/reservation/calendar-p2s"

response = requests.get(URL, timeout=30)
response.raise_for_status()

html = response.text

match = re.search(r'"P0814":"([BCN])"', html)

if match is None:
    raise Exception("P0814が見つかりません")

status = match.group(1)

print(f"P0814={status}")

if status == "B":
    print("空きあり")

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
