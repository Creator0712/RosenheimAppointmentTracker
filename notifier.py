import os
from dotenv import load_dotenv
from telegram import Bot
import asyncio

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


async def send_test_message():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(
        chat_id=CHAT_ID,
        text="✅ Rosenheim Appointment Tracker is working!"
    )


if __name__ == "__main__":
    asyncio.run(send_test_message())