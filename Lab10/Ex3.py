import requests

api_key = "f9a79194-9733-4df6-a725-7891a7e4a167"

response = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Москва,+Красная+площадь,+1&format=json")
json_response = response.json()
museum = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
museum_address = museum["metaDataProperty"]["GeocoderMetaData"]["text"]
museum_coodrinates = museum["Point"]["pos"]
print(museum_address, "    Координаты:", museum_coodrinates)