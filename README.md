# postcodes_io_api
A library that provides a Python interface to the postcodes_io API.

# Project URLs
 * Project Home : https://postcodes.io 
 * Project Doc  : https://postcodes.io/docs


# Api
```python
Api(self, debug_http=False, timeout=None, base_url=None)
```

## is_postcode_valid
```python
Api.is_postcode_valid(self, postcode)
```

This method validates post_code
* **:param postcode** - postcode to check i.e. 'SW112EF'
* **:return** - True if postcode is valid False if postcode is invalid

```
  is_valid = api.is_postcode_valid('SW112EF')

```

## is_postcode_terminated
```python
Api.is_postcode_terminated(self, postcode)
```

* **:param postcode** - postcode to check i.e. 'SW112ZW'
* **:return** True if postcode is terminated or False otherwise

```
  is_terminated = api.is_postcode_terminated('SW112EF')

```

## get_postcode
```python
Api.get_postcode(self, postcode)
```

This method returns data for post_code
* **:param postcode** - postcode to check i.e. 'SW112EF'
* **::return** - postcode detailed data
```
  data = api.get_postcode('SW112EF')

```

## get_nearest_postcodes_for_postcode
```python
Api.get_nearest_postcodes_for_postcode(self, **kwargs)
```

* **kwargs**
* **:param postcode** - postcode
* **:param limit** - (not required) Limits number of postcodes matches to return. Defaults to 10. Needs to be less than 100.
* **:param radius** -  (not required) Limits number of postcodes matches to return. Defaults to 100m. Needs to be less than 2,000m.
* **:return:** - list of nearest postcodes data

```
  data = api.get_nearest_postcodes_for_postcode(postcode='SW112EF',limit=2)

```

## get_nearest_postcodes_for_coordinates
```python
Api.get_nearest_postcodes_for_coordinates(self, **kwargs)
```

* **kwargs**
* **:param latitude** - (required) Latitude
* **:param longitude** - (required) Longitude
* **:param limit** - (not required) Limits number of postcodes matches to return. Defaults to 10. Needs to be less than 100.
* **:param radius** -  (not required) Limits number of postcodes matches to return. Defaults to 100m. Needs to be less
* **:return:** - list of nearest postcodes data

```
  data = api.get_nearest_postcodes_for_coordinates(latitude=51.466324,longitude=-0.173606,limit=2)

```


## get_bulk_postcodes
```python
Api.get_bulk_postcodes(self, postcodes_list)
```

* **:param postcodes_list** - list containing postcodes
* **:return** - list of postcode data

```
  postcode_list = ["SW112EF","HA97QP"]
  data = api.get_bulk_postcodes(postcode_list)

```

## get_bulk_reverse_geocode
```python
Api.get_bulk_reverse_geocode(self, payload_data)
```

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


## get_random_postcode
```python
Api.get_random_postcode(self)
```

* **:return** - random postcode

```
    data = api.get_random_postcode()
```

## get_autocomplete_postcode
```python
Api.get_autocomplete_postcode(self, **kwargs)
```

* **kwargs**
* **:param postcode** - partial postcode
* **:param limit** - (not required) Limits number of postcodes matches to return. Defaults to 10. Needs to be less than 100.
* **:return** -  list of possible postcodes

```
    data = api.get_autocomplete_postcode(postcode='SW18',limit=2)
```

## get_outcode
```python
Api.get_outcode(self, outcode)
```

This method returns data for post_code
* **:param outcode** - postcode outward code to check i.e. 'KT1'
* **:return** - postcode detailed data

```
    data = api.get_outcode('KT1')
```

## get_nearest_outcodes_for_outcode
```python
Api.get_nearest_outcodes_for_outcode(self, **kwargs)
```

* **kwargs**
* **:param outcode** - outward code
* **:param limit** - (not required) Limits number of postcodes matches to return. Defaults to 10. Needs to be less than 100.
* **:param radius** - (not required) Limits number of postcodes matches to return. Defaults to 100m. Needs to be less than 2,000m.
* **:return:** - list of nearest postcodes data

```
    data = api.get_nearest_outcodes_for_outcode(outcode='KT1',limit=2)
```

## get_nearest_outcodes_for_coordinates
```python
Api.get_nearest_outcodes_for_coordinates(self, **kwargs)
```

* **kwargs**
* **:param latitude** - (required) Latitude
* **:param longitude** - (required) Longitude
* **:param limit** - (not required) Limits number of postcodes matches to return. Defaults to 10. Needs to be less than 100.
* **:param radius** -  (not required) Limits number of postcodes matches to return. Defaults to 100m. Needs to be less
* **:return:** - list of nearest outcodes data

```
    data = api.get_nearest_outcodes_for_coordinates(latitude=51.466324,longitude=-0.173606,limit=2)
```

