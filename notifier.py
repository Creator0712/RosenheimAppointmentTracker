import os
import json
import asyncio
from dotenv import load_dotenv
from telegram import Bot
from win11toast import toast

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

JSON_FILE = "data/last_notification.json"


class Notifier:

    def __init__(self):
        self.bot = Bot(BOT_TOKEN)

    def get_last_notification(self):

        with open(JSON_FILE, "r") as f:
            data = json.load(f)

        return data["last_notified"]

    def save_notification(self, appointment_date):

        with open(JSON_FILE, "w") as f:
            json.dump(
                {
                    "last_notified": str(appointment_date)
                },
                f,
                indent=4
            )

    async def telegram(self, appointment_date):

        text = f"""
🚨 Earlier Appointment Found!

New Appointment:

{appointment_date}

Book Now:

https://www.etermin.net/stadt-rosenheim-stva-qtermin
"""

        await self.bot.send_message(
            chat_id=CHAT_ID,
            text=text
        )

    def windows(self, appointment_date):

        toast(
            "Rosenheim Appointment Tracker",
            f"Earlier appointment found!\n{appointment_date}"
        )