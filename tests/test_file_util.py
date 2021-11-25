import unittest
from src.file_util import *


class TestFileUtil(unittest.TestCase):
    # Test method to test the read_json_file function
    def test_read_json_file(self):
        # test case 1
        self.assertIsNotNone(read_json_file('test_files/test_good_file.txt'))

        # test case 2
        self.assertRaises(FileNotFoundError, read_json_file, 'test_no_such_file.txt')

        # test case 3
        self.assertRaises(json.decoder.JSONDecodeError, read_json_file, 'test_files/test_bad_file.txt')