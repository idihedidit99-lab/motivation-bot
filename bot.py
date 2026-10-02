import os, random, urllib.request, urllib.parse
from datetime import datetime
from zoneinfo import ZoneInfo

TZ = ZoneInfo("Asia/Irkutsk")   # иркутское время
START, END = 9, 22               # с 9:00 до 22:00

PHRASES = [
    "Чувак, ты должен работать.",
    "Ты делаешь это ради своей жизни. Двигайся.",
    "Час прошёл. Что ты сделал за него?",
    "Счастье не наступит само. Бери и делай.",
    "Хватит откладывать. Начинай прямо сейчас.",
    "Ты сильнее, чем думаешь. Действуй.",
]

hour = datetime.now(TZ).hour
if START <= hour < END:
    data = urllib.parse.urlencode({
        "chat_id": os.environ["CHAT_ID"],
        "text": random.choice(PHRASES),
    }).encode()
    url = f"https://api.telegram.org/bot{os.environ['BOT_TOKEN']}/sendMessage"
    urllib.request.urlopen(url, data)
