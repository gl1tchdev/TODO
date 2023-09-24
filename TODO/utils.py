from random import choice
from datetime import datetime
import string
import pytz


def generate_random_string(length: int = 6) -> str:
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    result_str = ''.join(choice(letters) for _ in range(length))
    return result_str


def get_datetime_obj(date_time: str) -> datetime:
    local = pytz.timezone("Europe/Moscow")
    format_str = '%Y-%m-%d %H:%M:%S'
    naive = datetime.strptime(date_time, format_str)
    local_dt = local.localize(naive, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)
    return utc_dt
