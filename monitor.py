from logger_config import logger
from datetime import datetime
import asyncio

from api import AppointmentAPI
from config import TARGET_DATE
from notifier import Notifier


def get_earliest_date():

    api = AppointmentAPI()

    appointments = api.get_available_dates()

    if not appointments:
        return None

    dates = []

    for appointment in appointments:

        d = datetime.strptime(
            appointment["start"][:10],
            "%Y-%m-%d"
        ).date()

        dates.append(d)

    return min(dates)


async def main():

    earliest = get_earliest_date()

    if earliest is None:
        print("No appointments.")
        return

    logger.info(f"Earliest appointment: {earliest}")

    if earliest >= TARGET_DATE:
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