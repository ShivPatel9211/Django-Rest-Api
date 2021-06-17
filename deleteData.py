import requests
import json
URL = 'http://localhost:8000/student/'


def delete_data():
    data = {
        'id':7,
    }
    json_data = json.dumps(data)
    res = requests.delete(url=URL, data=json_data)
    json_data = res.json()
    print(json_data)
delete_data()
