from src.common_util import *
from src.models import *


# Function to ingest each record and store in lists and dictionaries
def ingest(e, record, customers, site_visits, images, orders, amount_spent_dict, site_visits_dict,
           min_date, max_date):
    try:
        # Ingesting everything as the FAQ says - You are still required to ingest events even if they
        # are not consumed as part of this challenge.
        # If the event is customer, add the customer record to customer list
        print(f"Inserted record for event {e}, with key {record['key']}")
        if e == 'CUSTOMER':
            ingest_customers(record, customers)

        # If the event is site visit,
        # 1. Add the record to site visits list, not needed for LTV computation but may need it for future reports
        # 2. Maintain a dictionary to store number of visits by each customer to retrieve O(1)
        elif e == 'SITE_VISIT':
            ingest_site_visits(record, site_visits)
            ingest_site_visits_dict(record, site_visits_dict)
        # If the event is image, add the image record to images list, again may be needed for future reports

        elif e == 'IMAGE':
            images.append(Image(record['verb'], record['key'], record['event_time'], record['customer_id'],
                                record['camera_make'], record['camera_model']))

        # If the event is order,
        # 1. Add the record to orders list
        # 2. Maintain a dictionary to store amount spent by each customer to retrieve O(1)
        # 3. We also need min and max dates to know the total weeks
        elif e == 'ORDER':
            ingest_orders(record, orders)
            ingest_order_dict(record, amount_spent_dict)
            current_date = record['event_time'].split('T')[0]
            min_date = get_min_date(min_date, current_date)
            max_date = get_max_date(max_date, current_date)
        # If the code block comes here, we may not considered this event
        # Logging all the un-recognized events to analyze if it can be useful
        else:
            print(f"Unrecognized event {e}, for customer {record['customer_id']} ")
        return min_date, max_date
    except Exception as ex:
        print(f"Error occurred while reading event {e} key {record['key']}, Exception : {ex}")


# Function to ingest to customers list
def ingest_customers(record, customers):
    customers.append(Customer(record['verb'], record['key'], record['event_time'], record['last_name'],
                              record['adr_city'], record['adr_state']))


# Function to ingest to site visits list
def ingest_site_visits(record, site_visits):
    site_visits.append(SiteVisit(record['verb'], record['key'], record['event_time'],
                                 record['customer_id'],
                                 record['tags']))


# Function to maintain dictionary to store number of visits by each customer to retrieve O(1)
def ingest_site_visits_dict(record, site_visits_dict):
    if record['customer_id'] not in site_visits_dict:
        site_visits_dict[record['customer_id']] = 1
    else:
        site_visits_dict[record['customer_id']] += 1


# Function to ingest to images list
def ingest_images(record, images):
    images.append(Image(record['verb'], record['key'], record['event_time'], record['customer_id'],
                        record['camera_make'], record['camera_model']))


# Function to ingest to orders list
def ingest_orders(record, orders):
    orders.append(Order(record['verb'], record['key'], record['event_time'], record['customer_id'],
                        record['total_amount']))


# Function to maintain a dictionary to store amount spent by each customer to retrieve O(1)
def ingest_order_dict(record, amount_spent_dict):
    if record['customer_id'] not in amount_spent_dict:
        amount_spent_dict[record['customer_id']] = get_amount(record['total_amount'])
    else:
        amount_spent_dict[record['customer_id']] += get_amount(record['total_amount'])