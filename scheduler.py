import asyncio
import time
from datetime import datetime

import schedule

from logger_config import logger
from monitor import main


def job():
    current_hour = datetime.now().hour

    if 7 <= current_hour <= 21:
        logger.info("Checking appointments...")

        try:
            asyncio.run(main())

        except Exception:
            logger.exception("Monitoring failed.")

    else:
        logger.info("Outside monitoring hours.")


logger.info("Scheduler started.")

# Run immediately
job()

# Then every 2 hours
schedule.every(2).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(10)