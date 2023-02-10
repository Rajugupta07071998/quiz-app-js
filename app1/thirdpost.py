import  requests
import json

data={'username':'oooooooooooooo','email':'ooooooooooooooo@gmail.com'}
j_data=json.dumps(data)

r=requests.post(url="http://127.0.0.1:8000/postdata",data=j_data)

data=r.json()
print(data)