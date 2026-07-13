from datetime import date

# -------------------------
# Appointment Configuration
# -------------------------

TARGET_DATE = date(2026, 9, 16)

SERVICE_ID = 196621

BOOKING_URL = "https://www.etermin.net/stadt-rosenheim-stva-qtermin"

# -------------------------
# Scheduler
# -------------------------

CHECK_INTERVAL_HOURS = 2

START_HOUR = 7
END_HOUR = 21

TIMEZONE = "Europe/Berlin"

# -------------------------
# API
# -------------------------

BASE_URL = "https://www.etermin.net/api/timeslots"

HEADERS = {
    "accept": "application/json, text/plain",
    "referer": BOOKING_URL,
    "user-agent": "Mozilla/5.0",
    "webid": "stadt-rosenheim-stva-qtermin"
}