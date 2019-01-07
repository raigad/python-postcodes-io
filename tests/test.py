import unittest

import postcodes_io
import random


class PostcodeIOTest(unittest.TestCase):
    def setUp(self):
        self.api_client = postcodes_io.Api()
        self.VALID_POSTCODES = ['L40TH', 'SW151JF', 'SW195AG', 'KT185LQ', 'NW87JY', 'RG11LZ']
        self.INVALID_POSTCODES = ['HA9997QP', 'SW19OSZ', 'HA89NX', 'RG101LZ', 'SW12EF', 'L500QD']
        self.TERMINATED_POSTCODES = ['SW112ZW', 'HA89NX', 'IV23EH', 'BA12QT', 'OX13LA', 'SE109DB']

    def test_is_postcode_valid(self):
        self.assertTrue(self.api_client.is_postcode_valid(random.choice(self.VALID_POSTCODES)))
        self.assertFalse(self.api_client.is_postcode_valid(random.choice(self.INVALID_POSTCODES)))
        self.assertFalse(self.api_client.is_postcode_valid(random.choice(self.TERMINATED_POSTCODES)))

    def test_is_postcode_termminated(self):
        pass

    def tearDown(self):
        # close session to avoid 'ResourceWarning: unclosed <socket.socket'
        self.api_client._session.close()
