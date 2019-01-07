import unittest

import postcodes_io
import random


class PostcodeIOTest(unittest.TestCase):
    def setUp(self):
        self.api_client = postcodes_io.Api()
        self.VALID_POSTCODES = ['L40TH', 'SW151JF', 'SW195AG', 'KT185LQ', 'NW87JY', 'RG11LZ']
        self.INVALID_POSTCODES = ['HA9997QP', 'SW19OSZ', 'HA899NX', 'RG101LZ', 'SW12EF', 'L500QD']
        self.TERMINATED_POSTCODES = ['SW112ZW', 'HA89NX', 'IV23EH', 'BA12QT', 'OX13LA', 'SE109DB']

    def test_is_postcode_valid(self):
        self.assertTrue(self.api_client.is_postcode_valid(random.choice(self.VALID_POSTCODES)))
        self.assertFalse(self.api_client.is_postcode_valid(random.choice(self.INVALID_POSTCODES)))
        self.assertFalse(self.api_client.is_postcode_valid(random.choice(self.TERMINATED_POSTCODES)))

    def test_is_postcode_terminated(self):
        self.assertFalse(self.api_client.is_postcode_terminated(random.choice(self.VALID_POSTCODES)))
        self.assertFalse(self.api_client.is_postcode_terminated(random.choice(self.INVALID_POSTCODES)))
        self.assertTrue(self.api_client.is_postcode_terminated(random.choice(self.TERMINATED_POSTCODES)))

    def test_get_postcode(self):
        valid_data = self.api_client.get_postcode(random.choice(self.VALID_POSTCODES))
        self.assertEqual(200, valid_data.get('status', None), "Checking get postcode")
        invalid_data = self.api_client.get_postcode(random.choice(self.INVALID_POSTCODES))
        self.assertEqual(404, invalid_data.get('status', None), "Checking invalid postcode")
        terminated_data = self.api_client.get_postcode(random.choice(self.TERMINATED_POSTCODES))
        self.assertEqual(404, terminated_data.get('status', None), "Checking terminated postcode")

    def tearDown(self):
        """
            : close api_client session to avoid 'ResourceWarning: unclosed <socket.socket'
        """
        self.api_client._session.close()
