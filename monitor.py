from logger_config import logger
from datetime import datetime
import asyncio

from api import AppointmentAPI
from config import TARGET_DATE
from notifier import Notifier


def get_tracker_status():
    """
    Returns the current tracker status as a dictionary.
    """

    api = AppointmentAPI()

    appointments = api.get_available_dates()

    if not appointments:
        return {
            "earliest_date": None,
            "target_date": TARGET_DATE,
            "earlier_found": False,
            "checked_at": datetime.now()
        }

    dates = []

    for appointment in appointments:

        d = datetime.strptime(
            appointment["start"][:10],
            "%Y-%m-%d"
        ).date()

        dates.append(d)

    earliest = min(dates)

    return {
        "earliest_date": earliest,
        "target_date": TARGET_DATE,
        "earlier_found": earliest < TARGET_DATE,
        "checked_at": datetime.now()
    }


async def main():

    status = get_tracker_status()

    earliest = status["earliest_date"]

    if earliest is None:
        logger.info("No appointments available.")
        return

    logger.info(f"Earliest appointment: {earliest}")

    if not status["earlier_found"]:
        logger.info("No earlier appointment found.")
        return

    notifier = Notifier()

    last = notifier.get_last_notification()

    if str(earliest) == last:

        logger.info("Already notified about this appointment.")

        return

    await notifier.telegram(earliest)

    notifier.windows(earliest)

    notifier.save_notification(earliest)

    logger.warning("Earlier appointment found. Notification sent.")


if __name__ == "__main__":

    asyncio.run(main())