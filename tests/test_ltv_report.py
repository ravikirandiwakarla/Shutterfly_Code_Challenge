import unittest
from src.file_util import *
from src.ingest import ingest
from src.ltv_report import TopXSimpleLTVCustomers


class TestLtvReport(unittest.TestCase):
    # Test method to test the ingest function as well as the TopXSimpleLTVCustomers function We use the ingest
    # function output to pass as an input to TopXSimpleLTVCustomers function, so that we can test both functions
    # together
    def test_ingest_TopXSimpleLTVCustomers(self):
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
        data = read_json_file('test_files/test_good_file.txt')
        for record in data:
            min_date, max_date = ingest(record['type'], record, customers, site_visits, images,

                                        orders, amount_spent_dict, site_visits_dict, min_date, max_date)

        # assert customer list
        self.assertEqual(3, len(customers))
        self.assertEqual('96f55c7d8f42', customers[0].key)
        self.assertEqual('77f33c7d8f76', customers[1].key)
        self.assertEqual('33f33c7d8f76', customers[2].key)

        # assert image list
        self.assertEqual(3, len(images))
        self.assertEqual('96f55c7d8f42', images[0].customer_id)
        self.assertEqual('33f33c7d8f76', images[1].customer_id)
        self.assertEqual('33f33c7d8f76', images[2].customer_id)

        # assert site visits list
        self.assertEqual(4, len(site_visits))
        self.assertEqual('96f55c7d8f42', site_visits[0].customer_id)
        self.assertEqual('77f33c7d8f76', site_visits[1].customer_id)
        self.assertEqual('77f33c7d8f76', site_visits[1].customer_id)
        self.assertEqual('33f33c7d8f76', site_visits[2].customer_id)

        # assert orders list
        self.assertEqual(4, len(orders))
        self.assertEqual('96f55c7d8f42', orders[0].customer_id)
        self.assertEqual('77f33c7d8f76', orders[1].customer_id)
        self.assertEqual('33f33c7d8f76', orders[2].customer_id)
        self.assertEqual('33f33c7d8f76', orders[3].customer_id)

        # assert amount spent dictionary
        self.assertEqual(12.34, amount_spent_dict['96f55c7d8f42'])
        self.assertEqual(19.76, amount_spent_dict['77f33c7d8f76'])
        self.assertEqual(40.28, amount_spent_dict['33f33c7d8f76'])

        # assert site visits dictionary
        self.assertEqual(1, site_visits_dict['96f55c7d8f42'])
        self.assertEqual(1, site_visits_dict['77f33c7d8f76'])
        self.assertEqual(2, site_visits_dict['33f33c7d8f76'])

        # assert min_date and max_date
        self.assertEqual(min_date, '2020-01-06')
        self.assertEqual(max_date, '2020-12-12')

        # using above test method output to test TopXSimpleLTVCustomers function
        top_x_ltv_report = 2
        sorted_ltv = TopXSimpleLTVCustomers(top_x_ltv_report, customers, amount_spent_dict, site_visits_dict, min_date,
                                            max_date)
        for rec in sorted_ltv[:top_x_ltv_report]:
            # assert LTV
            self.assertEqual('33f33c7d8f76', sorted_ltv[0][0])

            '''
            A simple LTV can be calculated using the following equation 52(a) x t.
             Where is the average customer value per week (customer expenditures per visit (USD) x number of site visits 
             per week) and is the average customer lifespan. The average lifespan for Shutterfly is 10 years.
            '''

            # each values needed for LTV calculation, are already asserted
            self.assertEqual(427.46, sorted_ltv[0][1])  # 52 * (40.28/2) * (2/49) * 10
            self.assertEqual('77f33c7d8f76', sorted_ltv[1][0])
            self.assertEqual(209.70, sorted_ltv[1][1])  # 52 * (19.76/1) * (1/49)  * 10
            self.assertEqual('96f55c7d8f42', sorted_ltv[2][0])
            self.assertEqual(130.96, sorted_ltv[2][1])  # 52 * (12.34/1) * (1/49)  * 10
