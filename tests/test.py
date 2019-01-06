import unittest

import postcodes_io


class PostcodeIOTest(unittest.TestCase):
    def setUp(self):
        self.api_client = postcodes_io.Api()

    def test_is_postcode_valid(self):
        # valid postcode
        self.assertTrue(self.api_client.is_postcode_valid('SW112EF'))
        # invalid postcode
        self.assertFalse(self.api_client.is_postcode_valid('SW1112'))
        # terminated postcode
        self.assertFalse(self.api_client.is_postcode_valid('SW112ZW'))
