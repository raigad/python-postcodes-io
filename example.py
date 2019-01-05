#!/usr/bin/env python

import postcodes_io


api = postcodes_io.Api(debug_http=False)

postcode1 = 'SW112EF'
if api.validate_postcode(postcode1):
    print("postcode ="+ postcode1+ " is valid")
else:
    print("postcode =" + postcode1 + " is invalid")
postcode2= 'SW1122222'
if api.validate_postcode(postcode2):
    print("postcode ="+ postcode2+ " is valid")
else:
    print("postcode =" + postcode2 + " is invalid")

