
import requests
import logging

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
        """
        print("calling validate_postcode method")
        if len(postcode) > 4:
            return True
        else:
            return False