import requests
import json
URL = 'http://localhost:8000/student/'

def get_data(id = None):
    data={}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    res = requests.get(url=URL,data=json_data)
    json_data = res.json()
    print(json_data)
get_data()
