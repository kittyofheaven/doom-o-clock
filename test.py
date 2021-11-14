import requests as rq
import time

BASE = "https://doom-clock-api.herokuapp.com/"

response = rq.get(BASE + 'atmosphere')
print(response.status_code)
print(response.json())

response = rq.put(BASE + 'atmosphere', {'Year' : 2050, 'Month' : 11})
print(response.status_code)
print(response.json())