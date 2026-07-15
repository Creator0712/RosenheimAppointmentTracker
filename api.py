import time
import requests
from datetime import datetime, date

from config import (
    BASE_URL,
    HEADERS,
    SERVICE_ID,
    REQUEST_TIMEOUT,
    MAX_RETRIES,
    RETRY_DELAY
)
from logger_config import logger


class AppointmentAPI:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

    def _request(self, params):
        """
        Send a GET request to the eTermin API with automatic retries.
        """

        for attempt in range(1, MAX_RETRIES + 1):

            try:
                logger.info(
                    f"API request (Attempt {attempt}/{MAX_RETRIES})..."
                )

                response = self.session.get(
                    BASE_URL,
                    params=params,
                    timeout=REQUEST_TIMEOUT
                )

                response.raise_for_status()

                logger.info("API request successful.")

                return response.json()

            except requests.exceptions.RequestException as e:

                logger.warning(
                    f"API request failed (Attempt {attempt}/{MAX_RETRIES}): {e}"
                )

                if attempt < MAX_RETRIES:
                    logger.info(
                        f"Retrying in {RETRY_DELAY} seconds..."
                    )
                    time.sleep(RETRY_DELAY)

                else:
                    logger.error(
                        "Maximum retry attempts reached. Giving up."
                    )
                    raise

    def get_available_dates(self):

        params = {
            "date": datetime.today().strftime("%Y-%m-%d"),
            "serviceid": SERVICE_ID,
            "rangesearch": 1,
            "capacity": 1,
            "caching": "false",
            "duration": 0,
            "cluster": "false",
            "slottype": 0,
            "fillcalendarstrategy": 0,
            "showavcap": "false",
            "appfuture": 180,
            "appdeadline": 0,
            "msdcm": 0,
            "oneoff": "null",
            "appdeadlinewm": 0,
            "calendarid": ""
        }

        return self._request(params)

    def get_time_slots(self, appointment_date: date):

        params = {
            "date": appointment_date.strftime("%Y-%m-%d"),
            "serviceid": SERVICE_ID,
            "capacity": 1,
            "caching": "false",
            "duration": 0,
            "cluster": "false",
            "slottype": 0,
            "fillcalendarstrategy": 0,
            "showavcap": "false",
            "appfuture": 180,
            "appdeadline": 0,
            "msdcm": 0,
            "oneoff": "null",
            "appdeadlinewm": 0,
            "calendarid": ""
        }

        return self._request(params)


if __name__ == "__main__":

    api = AppointmentAPI()

    print("Available Dates:")
    print(api.get_available_dates())

    print("\nTime Slots:")
    print(api.get_time_slots(date(2026, 9, 10)))