from datetime import datetime
from django.utils.crypto import get_random_string
import pytz
from django.utils import timezone
from datetime import datetime
from dateutil.relativedelta import relativedelta

### this constant defines the only characters that the random string could contain
RANDOM_NUMBERS_STRING = '0123456789'

def generate_random_str( length: int) -> str:
    ''' This function returns a random string of given length and given characters'''
    return get_random_string(length=length, allowed_chars=RANDOM_NUMBERS_STRING)

def is_expired(start_date: datetime, minutes: int) -> bool:
    ''' This method checks if the deadline is passed or not'''
    deadline = start_date + relativedelta(minutes=minutes)

    return timezone.now().replace(tzinfo=pytz.UTC) > deadline.replace(tzinfo=pytz.UTC)
