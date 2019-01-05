#!/usr/bin/env python

import postcodes_io


api = postcodes_io.Api(debug_http=True)

postcode1 = 'SW112EF'
postcode2= 'SW112222'

"""
data1 = api.get_postcode(postcode1)
print(data1)
data2 = api.get_postcode(postcode2)
print(data2)
"""

"""
lat = 51.466324
lon = -0.173606
data = api.get_nearest_postcodes_for_coordinates(latitude=lat,longitude=lon,limit=2)
print(data)
"""

#data = api.get_bulk_postcodes({"postcodes":["OX49 5NU","M32 0JG","NE30 1DP"]})
list = ["SW112EF"]
data = api.get_bulk_postcodes(list)
print("\n")
print(data)

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


