import requests
import logging
import json
from urllib.parse import urlparse, urlunparse, urlencode, quote_plus
from urllib.request import __version__ as urllib_version
import http.client as http_client

API_BASE_URL = 'http://api.postcodes.io'


class Api(object):
    def __init__(self, debug_http=False, timeout=None, base_url=None):
        """
        Instantiate a new postcodes_io.Api object

        :param debug_http (bool, optional) enable logging for http requests.
        :param timeout (int, optional): set timeout for http/https requests

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

    def validate_postcode(self, postcode):
        """
        This method validates post_code
        :param postcode: postcode to check i.e. 'SW112EF'
        :return: True if postcode is valid False if postcode is invalid
        """
        url = '/postcodes/{postcode}/validate'.format(postcode=postcode)
        response = self._make_request('GET', url)
        data = self._parse_json_data(response.content.decode('utf-8'))
        return True if response.status_code == 200 and data.get('result') else False

    def get_postcode(self, postcode):
        """
        This method returns data for post_code
        :param postcode: postcode to check i.e. 'SW112EF'
        :return: postcode detailed data
        """
        url = '/postcodes/{postcode}'.format(postcode=postcode)
        response = self._make_request('GET', url)
        data = self._parse_json_data(response.content.decode('utf-8'))
        return data

    def get_nearest_postcodes_for_coordinates(self, **kwargs):
        """
        :param latitude: (required) Latitude
        :param longitude: (required) Longitude
        :param limit: (not required) Limits number of postcodes matches to return. Defaults to 10. Needs to be less than 100.
        :param radius: (not required) Limits number of postcodes matches to return. Defaults to 100m. Needs to be less than 2,000m.
        :return:
        """
        if kwargs.get('latitude') and kwargs.get('longitude'):
            url = '/postcodes'
            response = self._make_request('GET', url, data=kwargs)
            data = self._parse_json_data(response.content.decode('utf-8'))
            return data

    def get_bulk_postcodes(self, postcodes_list):
        """
        :param postcodes_list: list containing postcodes
        :return:
        """
        url = '/postcodes'
        response = self._make_request('POST', url, json={'postcodes': postcodes_list})
        data = self._parse_json_data(response.content.decode('utf-8'))
        return data

    def get_bulk_reverge_geocode(self, payload):
        pass

    def get_random_postcode(self):
        pass

    def get_nearest_postcodes_for_postcode(self, postcode):
        pass

    def get_autocomplete_postcode(self):
        pass

    def get_terminated_postcode(self, postcode):
        pass

    # outcodes methods
    def get_outcode(self, outcode):
        pass

    def get_nearest_outcodes_for_outcode(self, outcode):
        pass

    def get_outcodes_for_coordinates(self, **kwargs):
        pass

    # extra methods
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
