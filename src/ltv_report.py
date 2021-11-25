from src.common_util import get_total_weeks
from src.constants import *
from src.file_util import *
from src.ingest import ingest


# Function to generate the ltv report. This method will call ingest and TopXSimpleLTVCustomers functions
def generate_ltv_report():
    # Ingesting everything as the FAQ says - You are still required to ingest events even if they
    # are not consumed as part of this challenge.

    # Variable Declarations
    customers = []  # List to store all the customers
    site_visits = []  # List to store all the site visits
    images = []  # List to store all the images
    orders = []  # List to store all the orders
    amount_spent_dict = dict()  # Dictionary to store amount spent by customer to retrieve by O(1)
    site_visits_dict = dict()  # Dictionary to store number of site visits by customer to retrieve by O(1)
    min_date = None  # min_date and max_date are useful to get total number of weeks
    max_date = None

    # read input file
    data = read_json_file(INPUT_PATH)
    if data is not None:
        # Ingesting all the records fetched from input files
        print('Started ingestion')
        # Logging each record,can be too verbose and can slow down the application. Turn OFF if you do not need it.
        print('Logging each record,can be too verbose and can slow down the application. Turn OFF when you no need it')
        for record in data:
            min_date, max_date = ingest(record['type'], record, customers, site_visits, images,
                                        orders, amount_spent_dict, site_visits_dict, min_date, max_date)

        print(f'Generating ltv report for top {TOP_X_LTV_REPORT} '
              f'customers, Please change X value in constants file for your testing')

        sorted_ltv = TopXSimpleLTVCustomers(TOP_X_LTV_REPORT, customers, amount_spent_dict, site_visits_dict, min_date,
                                            max_date)

        print('Clearing the data present in the output file')
        # Clearing the data present in the output file
        # clear_file_data(OUTPUT_PATH)
        write_file("", OUTPUT_PATH, 'w')
        for rec in sorted_ltv[:TOP_X_LTV_REPORT]:
            write_file("Customer Id: {}         LTV: {} \n".format(rec[0], rec[1]), OUTPUT_PATH, 'a')
        print(f'LTV report successfully executed, please see the output path - {OUTPUT_PATH}')


# Function to run the top X customers based on their LTV
def TopXSimpleLTVCustomers(x, customers, amount_spent_dict, site_visits_dict, min_date, max_date):
    ltv_dict = dict()  # Dictionary to hold the LTV key value pairs
    print('Calculating total weeks used for this report')
    # Calculating total weeks used for this report
    total_weeks = get_total_weeks(min_date, max_date)
    print('Iterating each customer to calculate the LTV')
    # Iterating each customer to calculate the LTV
    for c in customers:

        # If no record in the site visit, then assuming the customer would have visited once
        customer_site_visits = 1 if c.key not in site_visits_dict.keys() else site_visits_dict[c.key]
        # If no record in the orders, then assuming amount spent is 0
        customer_amount_spent = 0 if c.key not in amount_spent_dict.keys() else amount_spent_dict[c.key]

        '''
        A simple LTV can be calculated using the following equation 52(a) x t.
         Where is the average customer value per week (customer expenditures per visit (USD) x number of site visits 
         per week) and is the average customer lifespan. The average lifespan for Shutterfly is 10 years.
        '''
        try:
            customer_amount_spent_per_visit = float((float(customer_amount_spent) / int(customer_site_visits)))
            ltv_value = round(52 * (customer_amount_spent_per_visit * (
                    int(customer_site_visits) / int(total_weeks)) * AVERAGE_LIFE_SPAN_SHUTTERFLY), 2)
            ltv_dict[c.key] = ltv_value
        except ValueError:
            ltv_value = 0

    return sorted(ltv_dict.items(), key=lambda y: y[1], reverse=True)


if __name__ == '__main__':
    generate_ltv_report()
