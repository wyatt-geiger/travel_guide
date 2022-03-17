import requests

def get_location(city, country):

    response = requests.get(f'https://api.mapbox.com/geocoding/v5/mapbox.places/{city},{country}.json?access_token=pk.eyJ1IjoibWFuZGlibGVjbGF3IiwiYSI6ImNrNmxpcWJ4MzBhamozZXBiZzVoNm11cmgifQ.lt7or9puZArJpANdrnIrUg').json()

    return response
    # returns values as a tuple. city is element 0, country is 1

def get_longitude_latitude(location_data): # this is used for the other APIs

    longitude = float(location_data['features'][0]['center'][0])

    latitude = float(location_data['features'][0]['center'][1])

    return longitude, latitude

