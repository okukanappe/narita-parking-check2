import os
import requests

USER = os.environ["PUSHOVER_USER"]
TOKEN = os.environ["PUSHOVER_TOKEN"]

requests.post(
    "https://api.pushover.net/1/messages.json",
    data={
        "token": TOKEN,
        "user": USER,
        "title": "GitHub Actions",
        "message": "🎉 テスト通知です！",
    },
)

print("通知を送信しました")
