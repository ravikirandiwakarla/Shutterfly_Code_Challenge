from datetime import date, timedelta
import datetime


# Function to get the min date
def get_min_date(min_date, current_date):
    min_date = current_date if min_date is None or current_date < min_date else min_date
    return min_date


# Function to get the max date
def get_max_date(max_date, current_date):
    max_date = current_date if max_date is None or current_date > max_date else max_date
    return max_date


# Function to get the total weeks using the min and max dates
def get_total_weeks(min_date, max_date):
    min_date = datetime.datetime.strptime(min_date, '%Y-%m-%d')
    max_date = datetime.datetime.strptime(max_date, '%Y-%m-%d')
    min_date = (min_date - timedelta(days=min_date.weekday() + 1))
    max_date = (max_date - timedelta(days=max_date.weekday() + 1))
    return int(((max_date - min_date).days / 7)) + 1


# Function to get the amount alone by excluding the currency
def get_amount(value):
    try:
        return float(value.split(' ')[0])
    except ValueError:
        return 0
