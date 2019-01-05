
import requests
import logging
import json


#TODO: could add support for python 2
from urllib.parse import urlparse, urlunparse, urlencode, quote_plus
from urllib.request import __version__ as urllib_version


logger = logging.getLogger(__name__)

class Api(object):

    def __init__(self,debug_http=False,timeout=None):
        """
        Instantiate a new postcodes_io.Api object
        Args:
            debug_http (bool, optional):
                Set to True to enable debug output from urllib2 when performing
                any HTTP requests.  Defaults to False.
            timeout (int, optional):
                Set timeout (in seconds) of the http/https requests. If None the
                requests lib default will be used.  Defaults to None.
        """
        self._debug_http = debug_http
        self._timeout = timeout

        if debug_http:
            try:
                import http.client as http_client #python 3
            except ImportError:
                import httplib as http_client #python 2

            http_client.HTTPConnection.debuglevel = 1

            logging.basicConfig()  # initialize logging
            logging.getLogger().setLevel(logging.DEBUG)
            requests_log = logging.getLogger("requests.packages.urllib3")
            requests_log.setLevel(logging.DEBUG)
            requests_log.propagate = True

        self._session = requests.Session()

    def validate_postcode(self,postcode):
        """
        This method validates post_code
        :param postcode: postcode to check i.e. 'SW112EF'
        """
        print("calling validate_postcode method")
        #if len(postcode) > 4:
        #    return True
        #else:
        #    return False


    def _make_request(self, http_method, url, data=None, json=None):
        """

        :param http_method: http method i.e. GET, POST, PUT etc
        :param url: api endpoint url
        :param data: dictionary of key/value params
        :param json:
        :return:
        """
        if not data:
            data = {}

        response = 0
        if http_method == 'GET':
            url = self._build_url(url, extra_params=data)
            response = self._session.get(url,timeout=self._timeout)
        elif http_method == 'POST':
            if data:
                response = self._session.post(url, data=data, timeout=self._timeout)
            elif json:
                response = self._session.post(url, json=json, timeout=self._timeout)

        return response

    def _build_url(self, url, path_elements=None, extra_params=None):
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

