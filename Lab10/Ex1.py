import requests

response = requests.get("https://static-maps.yandex.ru/1.x/?ll=86.093348%2C55.351368&spn=0.002,0.002&l=map")
print(response)
response = requests.get("https://static-maps.yandex.ru/1.x/?ll=86.195921%2C54.633625&spn=0.001,0.001&l=map")
print(response)
response = requests.get("https://static-maps.yandex.ru/1.x/?ll=2.294513%2C48.857747&spn=0.005,0.005&l=sat")
print(response)
response = requests.get("https://static-maps.yandex.ru/1.x/?ll=158.848938%2C53.255097&spn=0.025,0.025&l=sat")
print(response)
response = requests.get("https://static-maps.yandex.ru/1.x/?ll=108.655058%2C53.586278&spn=2.5,3.1&l=sat")
print(response)
response = requests.get("https://static-maps.yandex.ru/1.x/?ll=63.309865%2C45.947975&spn=0.05,0.05&l=sat")
print(response)