import requests
from django.conf import settings

BOT_TOKEN = "8453461184:AAG2MlqIu5waTZDot9VuSTAvuh9K1q2LeRs"  # bu yerga tokeningizni yozing
CHAT_ID = "1808774257"  # o‘zingizni chat_id (yoki guruh id) yozasiz

def send_to_telegram(message, photo_path=None):
    """Text va rasmni Telegramga yuboradi"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    photo_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

    if photo_path:
        files = {'photo': open(photo_path, 'rb')}
        data = {'chat_id': CHAT_ID, 'caption': message}
        requests.post(photo_url, data=data, files=files)
    else:
        data = {'chat_id': CHAT_ID, 'text': message}
        requests.post(url, data=data)
