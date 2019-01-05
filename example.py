#!/usr/bin/env python

import postcodes_io


api = postcodes_io.Api(debug_http=True)


print(api.validate_postcode('SW'))
print(api.validate_postcode('SW112ef'))
