from datetime import datetime
import os
import requests

filename = f'data/{datetime.utcnow().strftime("%Y%m%dT%H%MZ")}.json'
os.makedirs(os.path.dirname(filename), exist_ok=True)

url = 'https://catfact.ninja/fact'
response = requests.get(url)

if response.status_code == 200:
    print(response.content.decode('utf8'))
    with open(filename, 'w') as f:
        f.write(response.content.decode('utf8'))
else:
    print(f'Request failed with status code: {response.status_code}')
