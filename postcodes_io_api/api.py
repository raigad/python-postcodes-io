import requests
import logging
import json

try:
    # python 3
    import http.client as http_client
    from urllib.parse import urlparse, urlunparse, urlencode
except ImportError:
    # python 2
    import httplib as http_client
    from urlparse import urlparse, urlunparse
    from urllib import urlencode

API_BASE_URL = 'http://api.postcodes.io'


class Api(object):
    def __init__(self, debug_http=False, timeout=None, base_url=None):
        """
        Instantiate a new postcodes_io.Api object

        * **:param debug_http**  - boolean (optional) To enable logging for http requests
        * **:param timeout **  - int Set timeout for http/https requests

        """
        self._debug_http = debug_http
        self._timeout = timeout
        if base_url:
            self.base_url = base_url
        else:
            self.base_url = API_BASE_URL

        if debug_http:
            http_client.HTTPConnection.debuglevel = 1
            logging.basicConfig()  # initialize logging
            logging.getLogger().setLevel(logging.DEBUG)
            requests_log = logging.getLogger("requests.packages.urllib3")
            requests_log.setLevel(logging.DEBUG)
            requests_log.propagate = True
        self._session = requests.Session()

    def is_postcode_valid(self, postcode):
        """
        This method validates post_code
        * **:param postcode** - postcode to check i.e. 'SW112EF'
        * **:return** - True if postcode is valid False if postcode is invalid

        ```
          is_valid = api.is_postcode_valid('SW112EF')

        ```
        """
        url = '/postcodes/{postcode}/validate'.format(postcode=postcode)
        response = self._make_request('GET', url)
        data = self._parse_json_data(response.content.decode('utf-8'))
        return True if response.status_code == 200 and data.get('result') else False

    def is_postcode_terminated(self, postcode):
        """
        * **:param postcode** - postcode to check i.e. 'SW112ZW'
        * **:return** True if postcode is terminated or False otherwise

        ```
          is_terminated = api.is_postcode_terminated('SW112EF')

        ```
        """
        url = '/terminated_postcodes/{postcode}'.format(postcode=postcode)
        response = self._make_request('GET', url)
        data = self._parse_json_data(response.content.decode('utf-8'))
        return True if response.status_code == 200 and data.get('result', {}).get('postcode') else False

    def get_postcode(self, postcode):
        """
        This method returns data for post_code
        * **:param postcode** - postcode to check i.e. 'SW112EF'
        * **::return** - postcode detailed data
        ```
          data = api.get_postcode('SW112EF')

        ```
        """
        url = '/postcodes/{postcode}'.format(postcode=postcode)
        response = self._make_request('GET', url)
        data = self._parse_json_data(response.content.decode('utf-8'))
        return data

    def get_nearest_postcodes_for_postcode(self, **kwargs):
        """
        * **kwargs**
        * **:param postcode** - postcode
        * **:param limit** - (not required) Limits number of postcodes matches to return. Defaults to 10. Needs to be less than 100.
        * **:param radius** -  (not required) Limits number of postcodes matches to return. Defaults to 100m. Needs to be less than 2,000m.
        * **:return:** - list of nearest postcodes data

        ```
          data = api.get_nearest_postcodes_for_postcode(postcode='SW112EF',limit=2)

        ```
        """
        url = '/postcodes/{postcode}/nearest'.format(postcode=kwargs.pop('postcode', ''))
        response = self._make_request('GET', url, data=kwargs)
        data = self._parse_json_data(response.content.decode('utf-8'))
        return data

    def get_nearest_postcodes_for_coordinates(self, **kwargs):
        """
        * **kwargs**
        * **:param latitude** - (required) Latitude
        * **:param longitude** - (required) Longitude
        * **:param limit** - (not required) Limits number of postcodes matches to return. Defaults to 10. Needs to be less than 100.
        * **:param radius** -  (not required) Limits number of postcodes matches to return. Defaults to 100m. Needs to be less
        * **:return:** - list of nearest postcodes data

        ```
          data = api.get_nearest_postcodes_for_coordinates(latitude=51.466324,longitude=-0.173606,limit=2)

        ```

        """
        if kwargs.get('latitude') and kwargs.get('longitude'):
            url = '/postcodes'
            response = self._make_request('GET', url, data=kwargs)
            data = self._parse_json_data(response.content.decode('utf-8'))
            return data

    def get_bulk_postcodes(self, postcodes_list):
        """
        * **:param postcodes_list** - list containing postcodes
        * **:return** - list of postcode data

        ```
          postcode_list = ["SW112EF","HA97QP"]
          data = api.get_bulk_postcodes(postcode_list)

        ```
        """
        url = '/postcodes'
        response = self._make_request('POST', url, json={'postcodes': postcodes_list})
        data = self._parse_json_data(response.content.decode('utf-8'))
        return data

    def get_bulk_reverse_geocode(self, payload_data):
        """
        * **:param payload_data** - dict with cordinates e.g.
        ```
        payload_data = {
        "geolocations":
        [
            {
                "longitude": 0.629834723775309,
                "latitude": 51.7923246977375
            },
            {
                "longitude": -2.49690382054704,
                "latitude": 53.5351312861402,
                "radius": 1000,
                "limit": 5
            }
        ]
        }
        ```
        * **:return** - list of postcode data

        ```
            data = api.get_bulk_reverse_geocode(payload_data)
        ```

        """
        url = '/postcodes'
        response = self._make_request('POST', url, json=payload_data)
        data = self._parse_json_data(response.content.decode('utf-8'))
        return data

    def get_random_postcode(self):
        """
        * **:return** - random postcode

        ```
            data = api.get_random_postcode()
        ```
        """
        url = '/random/postcodes'
        response = self._make_request('GET', url)
        data = self._parse_json_data(response.content.decode('utf-8'))
        return data

    def get_autocomplete_postcode(self, **kwargs):
        """
        * **kwargs**
        * **:param postcode** - partial postcode
        * **:param limit** - (not required) Limits number of postcodes matches to return. Defaults to 10. Needs to be less than 100.
        * **:return** -  list of possible postcodes

        ```
            data = api.get_autocomplete_postcode(postcode='SW18',limit=2)
        ```
        """
        url = '/postcodes/{postcode}/autocomplete'.format(postcode=kwargs.pop('postcode', ''))
        response = self._make_request('GET', url, data=kwargs)
        data = self._parse_json_data(response.content.decode('utf-8'))
        return data

    def get_outcode(self, outcode):
        """
        This method returns data for post_code
        * **:param outcode** - postcode outward code to check i.e. 'KT1'
        * **:return** - postcode detailed data

        ```
            data = api.get_outcode('KT1')
        ```
        """
        url = '/outcodes/{outcode}'.format(outcode=outcode)
        response = self._make_request('GET', url)
        data = self._parse_json_data(response.content.decode('utf-8'))
        return data

    def get_nearest_outcodes_for_outcode(self, **kwargs):
        """
        * **kwargs**
        * **:param outcode** - outward code
        * **:param limit** - (not required) Limits number of postcodes matches to return. Defaults to 10. Needs to be less than 100.
        * **:param radius** - (not required) Limits number of postcodes matches to return. Defaults to 100m. Needs to be less than 2,000m.
        * **:return:** - list of nearest postcodes data

        ```
            data = api.get_nearest_outcodes_for_outcode(outcode='KT1',limit=2)
        ```
        """
        url = '/outcodes/{outcode}/nearest'.format(outcode=kwargs.pop('outcode', ''))
        response = self._make_request('GET', url, data=kwargs)
        data = self._parse_json_data(response.content.decode('utf-8'))
        return data

    def get_nearest_outcodes_for_coordinates(self, **kwargs):
        """
        * **kwargs**
        * **:param latitude** - (required) Latitude
        * **:param longitude** - (required) Longitude
        * **:param limit** - (not required) Limits number of postcodes matches to return. Defaults to 10. Needs to be less than 100.
        * **:param radius** -  (not required) Limits number of postcodes matches to return. Defaults to 100m. Needs to be less
        * **:return:** - list of nearest outcodes data

        ```
            data = api.get_nearest_outcodes_for_coordinates(latitude=51.466324,longitude=-0.173606,limit=2)
        ```
        """
        if kwargs.get('latitude') and kwargs.get('longitude'):
            url = '/outcodes'
            response = self._make_request('GET', url, data=kwargs)
            data = self._parse_json_data(response.content.decode('utf-8'))
            return data

    # TODO: add extra method to get haversine distance between postcodes using their coordinates
    def get_distance_between_postcodes(self, **kwargs):
        pass

    def _make_request(self, http_method, url, data=None, json=None):
        """
        :param http_method: http method i.e. GET, POST, PUT etc
        :param url: api endpoint url
        :param data: dictionary of key/value params
        :param json: json data
        :return:
        """
        if not data:
            data = {}

        response = 0
        if http_method == 'GET':
            url = self._build_url(url, extra_params=data)
            response = self._session.get(url, timeout=self._timeout)
        elif http_method == 'POST':
            url = self._build_url(url)
            if data:
                response = self._session.post(url, data=data, timeout=self._timeout)
            elif json:
                response = self._session.post(url, json=json, timeout=self._timeout)
        return response

    def _build_url(self, url, path_elements=None, extra_params=None):
        url = self.base_url + url
        (scheme, netloc, path, params, query, fragment) = urlparse(url)

        # Add extra_parameters to the query
        if extra_params and len(extra_params) > 0:
            extra_query = self._encode_parameters(extra_params)
            if query:
                query += '&' + extra_query
            else:
                query = extra_query
        return urlunparse((scheme, netloc, path, params, query, fragment))

    @staticmethod
    def _encode_parameters(parameters):
        """
        Return url encoded string in 'key=value&key=value' format
        """
        if not parameters or not isinstance(parameters, dict):
            return None
        return urlencode(parameters)

    @staticmethod
    def _parse_json_data(json_data):
        try:
            data = json.loads(json_data)
        except ValueError:
            data = json.loads('{"Error": "Unknown error while parsing response"}')
        return data
