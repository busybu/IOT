import matplotlib.pyplot as plt
import pyodbc
import time
import requests
import numpy as np

server = 'CT-C-00186\SQLEXPRESS'
database = 'tempdb' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')

def sinal():
    proxies = {'https':"https://disrct:etsds10243110@10.224.200.26:8080"}
    url_temperatura = 'https://iot-tds2-default-rtdb.firebaseio.com/Gabrielle/Sensor/temperatura.json'
    url_umidade= 'https://iot-tds2-default-rtdb.firebaseio.com/Gabrielle/Sensor/umidade.json'
    temperatura = float(requests.get(url_temperatura, proxies=proxies).content)
    umidade = float(requests.get(url_umidade,proxies=proxies).content)
    return temperatura, umidade

def InserirBD(sinal):
    global cnxn
    cursor = cnxn.cursor()
    cursor.execute(f"INSERT dbo.Sensor (Temperatura, Umidade) VALUES ({sinal[0]},{sinal[1]});")
    cnxn.commit()
    print("Inserido com sucesso!")

def SelectBD():
    global cnxn
    cursor = cnxn.cursor()
    cursor.execute("SELECT Temperatura, timestamp FROM dbo.Sensor")
    row = cursor.fetchone()
    lista = []
    listatempo = []
    while row: 
        lista.append(row[0])
        listatempo.append(str(row[1]))
        row = cursor.fetchone()

def apresentar(sinal):
    print(f"Temperatura: {sinal[0]}")
    print(f"Umidade: {sinal[1]}")
    
while True:
    valores = sinal()
    apresentar(valores)
    InserirBD(valores)
    time.sleep(120)