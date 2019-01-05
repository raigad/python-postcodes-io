#!/usr/bin/env python

import postcodes_io


api = postcodes_io.Api(debug_http=False)

postcode1 = 'SW112EF'
postcode2= 'SW1122222'

data1 = api.get_postcode(postcode1)
print(data1)
data2 = api.get_postcode(postcode2)
print(data2)
"""
if api.validate_postcode(postcode1):
    print("postcode ="+ postcode1+ " is valid")
else:
    print("postcode =" + postcode1 + " is invalid")

if api.validate_postcode(postcode2):
    print("postcode ="+ postcode2+ " is valid")
else:
    print("postcode =" + postcode2 + " is invalid")
"""


