import requests
from datetime import datetime, date
from config import BASE_URL, HEADERS, SERVICE_ID


class AppointmentAPI:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

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

        response = self.session.get(
            BASE_URL,
            params=params,
            timeout=20
        )

        response.raise_for_status()

        return response.json()

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

        response = self.session.get(
            BASE_URL,
            params=params,
            timeout=20
        )

        response.raise_for_status()

        return response.json()


if __name__ == "__main__":

    api = AppointmentAPI()

    print("Available Dates:")
    print(api.get_available_dates())

    print("\nTime Slots:")
    print(api.get_time_slots(date(2026, 9, 16)))