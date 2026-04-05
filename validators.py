import re
from datetime import datetime

EMAIL_PATTERN = r"^[\w\.]+@[\w\.]+\.[a-zA-Z]{2,}$"
EGYPTIAN_PHONE_PATTERN = r"^(\+20|0)?1[0125][0-9]{8}$"
DATE_FORMAT = "%Y-%m-%d"


def is_valid_email(email):
    return bool(re.match(EMAIL_PATTERN, email))


def is_valid_egyptian_phone(phone):
    return bool(re.match(EGYPTIAN_PHONE_PATTERN, phone))


def passwords_match(password, confirm_password):
    return password == confirm_password


def parse_valid_date(date_str):
    try:
        return datetime.strptime(date_str, DATE_FORMAT)
    except ValueError:
        return None
