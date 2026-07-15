import os
import json
import platform

from dotenv import load_dotenv
from telegram import Bot

from config import BOOKING_URL, TARGET_DATE
from logger_config import logger

# -------------------------
# Windows Notifications
# -------------------------

if platform.system() == "Windows":
    from win11toast import toast
else:
    toast = None

# -------------------------
# Environment
# -------------------------

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# -------------------------
# Files
# -------------------------

DATA_FOLDER = "data"
JSON_FILE = os.path.join(DATA_FOLDER, "last_notification.json")

os.makedirs(DATA_FOLDER, exist_ok=True)

if not os.path.exists(JSON_FILE):
    with open(JSON_FILE, "w") as f:
        json.dump(
            {
                "last_notified": None
            },
            f,
            indent=4
        )


class Notifier:

    def __init__(self):
        self.bot = Bot(BOT_TOKEN)

    def get_last_notification(self):

        with open(JSON_FILE, "r") as f:
            data = json.load(f)

        return data.get("last_notified")

    def save_notification(self, appointment_date):

        with open(JSON_FILE, "w") as f:
            json.dump(
                {
                    "last_notified": str(appointment_date)
                },
                f,
                indent=4
            )

        logger.info("Notification history updated.")

    async def telegram(self, appointment_date):

        text = (
            "🚨 Earlier Appointment Found!\n\n"
            f"📅 Current Appointment:\n{TARGET_DATE}\n\n"
            f"✅ Earlier Appointment:\n{appointment_date}\n\n"
            f"🔗 Book Now:\n{BOOKING_URL}\n\n"
            "Good luck! 🍀"
        )

        await self.bot.send_message(
            chat_id=CHAT_ID,
            text=text
        )

        logger.info("Telegram notification sent.")

    def windows(self, appointment_date):

        if toast is None:
            return

        toast(
            "Rosenheim Appointment Tracker",
            f"Earlier appointment found!\n{appointment_date}"
        )

        logger.info("Windows notification sent.")