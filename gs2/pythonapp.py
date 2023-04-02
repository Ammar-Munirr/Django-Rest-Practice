import requests
import json

url = 'http://127.0.0.1:8000/api/stucreate/'

data = {
    'name':'ali',
    'roll':33,
    'city':'Muridke'
}

json_data = json.dumps(data)
 
r = requests.post(url=url,data=json_data)
