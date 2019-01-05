#!/usr/bin/env python

import postcodes_io


api = postcodes_io.Api()

print(api.validate_postcode('SW'))
print(api.validate_postcode('SW112ef'))
