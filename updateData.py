import requests
import json
URL = 'http://localhost:8000/student/'


def update_data():
    data = {
        'id':7,
        'name':'Patel',
        'roll':106,
        'city': 'Balinagar'
    }
    json_data = json.dumps(data)
    res = requests.put(url=URL, data=json_data)
    json_data = res.json()
    print(json_data)
update_data()
