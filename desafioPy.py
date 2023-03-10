import requests
import json

url_temperatura = 'https://iot-tds2-default-rtdb.firebaseio.com/Gabrielle/Sensor/temperatura.json'
url_umidade= 'https://iot-tds2-default-rtdb.firebaseio.com/Gabrielle/Sensor/umidade.json'

nome = input('Insira um nome:')

 
proxies = {'https':"https://disrct:etsds10243110@10.224.200.26:8080"}
url = f'https://api.agify.io?name={nome}'
request = requests.get(url, proxies=proxies)
data = request.json()

print(f'{nome}, {data[]} anos.')