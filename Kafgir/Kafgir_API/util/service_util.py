from datetime import datetime
from django.utils.crypto import get_random_string
import pytz
from datetime import datetime
from dateutil.relativedelta import relativedelta

def generate_random_str( length: int) -> str:
    return get_random_string(length=length)

def is_expired(start_date: datetime, minutes: int) -> bool:
    deadline = start_date + relativedelta(minutes=minutes)

    return datetime.now().replace(tzinfo=pytz.UTC) > deadline.replace(tzinfo=pytz.UTC)
