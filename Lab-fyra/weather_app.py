import requests
from random import randint

url = 'http://127.0.0.1:5000/postjson' #Servern för vädret

# Simulate sensor data into json format
for i in range(10):
    sensdata_dict= {
        "sensor" : "BME280",
        "temperature" : randint(-10,10),
        "humidity" : randint(60,100),
        "pressure" : randint(1019,1028),
        "wind" : randint(0,10)
        }
    r = requests.post(url, json=sensdata_dict)
    print(r.status_code)
