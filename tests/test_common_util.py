import unittest
from src.common_util import *


class TestCommonUtil(unittest.TestCase):

    # Test method to test the get_min_date function
    def test_get_min_date(self):
        # test case 1
        self.assertEqual('2020-05-05', get_min_date('2020-05-05', '2020-08-12'))

        # test case 2
        self.assertEqual('2020-05-05', get_min_date('2020-08-12', '2020-05-05'))

    # Test method to test the get_max_date function
    def test_get_max_date(self):
        # test case 1
        self.assertEqual('2020-08-12', get_max_date('2020-05-05', '2020-08-12'))

        # test case 2
        self.assertEqual('2020-08-12', get_max_date('2020-08-12', '2020-05-05'))

    # Test method to test the get_total_weeks function
    def test_get_total_weeks(self):
        # test case 1
        self.assertEqual(2, get_total_weeks('2020-05-02', '2020-05-05'))

        # test case 2
        self.assertEqual(15, get_total_weeks('2020-05-05', '2020-08-12'))

        # test case 3
        self.assertEqual(49, get_total_weeks('2020-01-06', '2020-12-12'))

    # Test method to test the get_amount function
    def test_get_amount(self):
        # test case 1
        self.assertEqual(12.34, get_amount('12.34 USD'))

        # test case 2
        self.assertEqual(0, get_amount('USD'))