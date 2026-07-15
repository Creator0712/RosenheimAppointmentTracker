from datetime import date

# -------------------------
# Appointment Configuration
# -------------------------

TARGET_DATE = date(2026, 9, 10)

SERVICE_ID = 196621

BOOKING_URL = "https://www.etermin.net/stadt-rosenheim-stva-qtermin"

# -------------------------
# Scheduler
# -------------------------

CHECK_INTERVAL_MINUTES = 30

START_HOUR = 7
END_HOUR = 21

TIMEZONE = "Europe/Berlin"

# -------------------------
# API
# -------------------------

BASE_URL = "https://www.etermin.net/api/timeslots"

REQUEST_TIMEOUT = 20

MAX_RETRIES = 3
RETRY_DELAY = 5


HEADERS = {
    "accept": "application/json, text/plain",
    "referer": BOOKING_URL,
    "user-agent": "Mozilla/5.0",
    "webid": "stadt-rosenheim-stva-qtermin"
}

# -------------------------
# NOTIFICATIONS
# -------------------------
ENABLE_TELEGRAM = True

ENABLE_WINDOWS_NOTIFICATION = True

# -------------------------
# APP
# -------------------------
APP_VERSION = "0.9.0"
LOG_LEVEL = "INFO"