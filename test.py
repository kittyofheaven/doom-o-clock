import requests as rq
import time

BASE = "http://127.0.0.1:5000/"

response = rq.put(BASE + 'atmosphere', {'Year' : 2008, 'Month' : 11})
print(response.status_code)
print(response.json())