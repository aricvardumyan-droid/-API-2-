import sys
from io import BytesIO
import requests
from PIL import Image
from spn import to_spn

toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {"apikey": "7eb1332d-4876-4b40-b314-76834f59eef7", "geocode": toponym_to_find, "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)
if not response:
    pass

json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
toponym_coodrinates = toponym["Point"]["pos"]
toponym_longitude, toponym_lattitude = map(float, toponym_coodrinates.split(" "))

spn = to_spn(toponym)

apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"

map_params = {
    "ll": f'{toponym_longitude},{toponym_lattitude}',
    "spn": f'{spn[0]},{spn[1]}',
    "apikey": apikey,
    'pt': f'{toponym_longitude},{toponym_lattitude},pm2dgm',
}

map_api_server = "https://static-maps.yandex.ru/v1"
response = requests.get(map_api_server, params=map_params)
im = BytesIO(response.content)
opened_image = Image.open(im)
opened_image.show()
