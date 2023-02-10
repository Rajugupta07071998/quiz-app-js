import requests

r=requests.get(url="http://127.0.0.1:8000/getdata")

#data=r.json()

print(r.json())
