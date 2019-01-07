import unittest

import postcodes_io_api
import random


class PostcodeIOTest(unittest.TestCase):
    def setUp(self):
        self.api_client = postcodes_io_api.Api()
        self.latitude = 51.466324
        self.longitude = -0.173606
        self.VALID_OUTCODES = ['KT19', 'HA9', 'SW19', 'IV2', 'PH16']
        self.VALID_POSTCODES = ['L40TH', 'SW151JF', 'SW195AG', 'KT185LQ', 'NW87JY', 'RG11LZ']
        self.INVALID_POSTCODES = ['HA9997QP', 'SW19OSZ', 'HA899NX', 'RG101LZ', 'SW12EF', 'L500QD']
        self.TERMINATED_POSTCODES = ['SW112ZW', 'HA89NX', 'IV23EH', 'BA12QT', 'OX13LA', 'SE109DB']
        self.reverse_geocode_data = {
            "geolocations": [{
                "longitude": 0.629834723775309,
                "latitude": 51.7923246977375
            }, {
                "longitude": -2.49690382054704,
                "latitude": 53.5351312861402,
                "radius": 1000,
                "limit": 5
            }]
        }

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
        self.assertEqual(200, valid_data.get('status', None), "Checking for valid postcode")
        invalid_data = self.api_client.get_postcode(random.choice(self.INVALID_POSTCODES))
        self.assertEqual(404, invalid_data.get('status', None), "Checking for invalid postcode")
        terminated_data = self.api_client.get_postcode(random.choice(self.TERMINATED_POSTCODES))
        self.assertEqual(404, terminated_data.get('status', None), "Checking for terminated postcode")

    def test_get_nearest_postcodes_for_postcode(self):
        data = self.api_client.get_nearest_postcodes_for_postcode(postcode=random.choice(self.VALID_POSTCODES), limit=2)
        self.assertEqual(200, data.get('status', None), "Checking for valid postcode")

    def test_get_nearest_postcodes_for_coordinates(self):
        data = self.api_client.get_nearest_postcodes_for_coordinates(latitude=self.latitude, longitude=self.longitude,
                                                                     limit=3)
        self.assertEqual(200, data.get('status', None))

    def test_get_bulk_postcodes(self):
        bulk_postcodes = [random.choice(self.VALID_POSTCODES), random.choice(self.VALID_POSTCODES)]
        data = self.api_client.get_bulk_postcodes(bulk_postcodes)
        self.assertEqual(200, data.get('status', None), "Checking for valid postcode")
        self.assertEqual(2, len(data.get('result', [])), "Checking for result count")

    def test_get_bulk_reverse_geocode(self):
        data = self.api_client.get_bulk_reverse_geocode(self.reverse_geocode_data)
        self.assertEqual(200, data.get('status', None))
        self.assertEqual(2, len(data.get('result', [])), "Checking for result count")

    def test_get_random_postcode(self):
        data = self.api_client.get_random_postcode()
        self.assertEqual(200, data.get('status', None))

    def test_get_autocomplete_postcode(self):
        data = self.api_client.get_autocomplete_postcode(postcode=random.choice(self.VALID_OUTCODES), limit=3)
        self.assertEqual(200, data.get('status', None))
        self.assertEqual(3, len(data.get('result', [])), "Checking for result count")

    def test_get_outcode(self):
        data = self.api_client.get_outcode(random.choice(self.VALID_OUTCODES))
        self.assertEqual(200, data.get('status', None), "Checking for valid outcode")

    def test_get_nearest_outcodes_for_outcode(self):
        data = self.api_client.get_nearest_outcodes_for_outcode(outcode=random.choice(self.VALID_OUTCODES))
        self.assertEqual(200, data.get('status', None), "Checking for valid outcode")

    def test_get_nearest_outcodes_for_coordinates(self):
        data = self.api_client.get_nearest_outcodes_for_coordinates(latitude=self.latitude, longitude=self.longitude,
                                                                    limit=3)
        self.assertEqual(200, data.get('status', None))
        self.assertEqual(3, len(data.get('result', [])), "Checking for result count")

    def tearDown(self):
        """
            : close api_client session to avoid 'ResourceWarning: unclosed <socket.socket'
        """
        self.api_client._session.close()
