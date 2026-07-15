import asyncio
import platform
import time
from datetime import datetime

import schedule

from logger_config import logger
from monitor import main
from config import (
    CHECK_INTERVAL_HOURS,
    START_HOUR,
    END_HOUR,
    TARGET_DATE
)

APP_VERSION = "0.9.1"


def print_startup_banner():
    logger.info("=" * 55)
    logger.info("Rosenheim Appointment Tracker")
    logger.info(f"Version              : {APP_VERSION}")
    logger.info(f"Platform             : {platform.system()}")
    logger.info(f"Monitoring Target    : Earlier than {TARGET_DATE}")
    logger.info(f"Monitoring Hours     : {START_HOUR}:00 - {END_HOUR}:00")
    logger.info(f"Check Interval       : Every {CHECK_INTERVAL_HOURS} hour(s)")
    logger.info("=" * 55)


def job():

    current_time = datetime.now()
    current_hour = current_time.hour

    if START_HOUR <= current_hour <= END_HOUR:

        logger.info("-" * 55)
        logger.info(
            f"Checking appointments ({current_time.strftime('%d-%m-%Y %H:%M:%S')})"
        )

        try:

            asyncio.run(main())

            logger.info("Monitoring cycle completed successfully.")

        except Exception:

            logger.exception("Monitoring cycle failed.")

    else:

        logger.info(
            f"Outside monitoring hours ({START_HOUR}:00 - {END_HOUR}:00). Skipping check."
        )


if __name__ == "__main__":

    print_startup_banner()

    logger.info("Scheduler started.")

    # First check immediately
    job()

    # Continue checking every configured interval
    schedule.every(CHECK_INTERVAL_HOURS).hours.do(job)

    while True:

        schedule.run_pending()

        time.sleep(10)