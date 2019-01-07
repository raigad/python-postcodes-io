#!/usr/bin/env python

import postcode-io-api

api = postcode-io-api.Api(debug_http=True)

postcode1 = 'SW112EF'
postcode2 = 'SW112222'


data1 = api.get_postcode(postcode1)
print("\n\n",data1)
#data2 = api.get_postcode(postcode2)
#print(data2)

#run only certain tests
#python setup.py test -s tests.test.PostcodeIOTest.test_get_postcode

"""
lat = 51.466324
lon = -0.173606
data = api.get_nearest_postcodes_for_coordinates(latitude=lat,longitude=lon,limit=2)
print(data)
"""
"""
#data = api.get_bulk_postcodes({"postcodes":["OX49 5NU","M32 0JG","NE30 1DP"]})
list = ["SW112EF"]
data = api.get_bulk_postcodes(list)
print("\n")
print(data)
"""

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

"""
#get random postcode
postcode_data = api.get_random_postcode()
print("random_postcode\n\n",postcode_data)
"""
"""
#get get_nearest_postcodes_for_postcode
data = api.get_nearest_postcodes_for_postcode(postcode='SW112EF')
print("\n",data)
"""

"""
#get
data =api.get_autocomplete_postcode(postcode='SW112E')
print("\n\n",data)
"""
"""
terminated_postcode = 'SW11 2ZW'
#terminated_postcode = 'SW112EF'
if api.is_postcode_terminated(terminated_postcode):
    print(terminated_postcode+" is_terminated")
else:
    print(terminated_postcode+" is_working_postcode")
"""

"""
payload_data = {
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
data = api.get_bulk_reverse_geocode(payload_data)
print("\n\n",data)
"""

"""
outcode = 'KT1'
data  = api.get_outcode(outcode)
print("\n\n",data)
"""

"""
outcode = 'KT1'
data = api.get_nearest_outcodes_for_outcode(outcode=outcode,limit=2)
print("\n\n",data)
"""

"""
lat = 51.466324
lon = -0.173606
data = api.get_nearest_outcodes_for_coordinates(latitude=lat,longitude=lon,limit=1)
print("\n\n",data)
"""

