from datetime import datetime
from datetime import timedelta

def add_gigasecond(time):
    futuretime = time + timedelta(seconds=10**9)
    return futuretime
