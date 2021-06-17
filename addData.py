import requests
import json
URL = 'http://localhost:8000/student/'


def add_data():
    data = {
        'name': 'Patel',
        'roll': 108,
        'city': 'RamNagar',
    }
    json_data = json.dumps(data)
    res = requests.post(url=URL, data=json_data)
    json_data = res.json()
    print(json_data)
add_data()
