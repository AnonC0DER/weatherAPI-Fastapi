import json
import random
import requests
import time
from requests.adapters import HTTPAdapter
from threading import Thread

def main(thread):
    url = 'http://167.235.19.250:30378/api/reports'
    
    with open('test.json', 'r') as fp:
        data = json.loads(fp.read())['data']
    
    status = ['rain', 'cloud', 'rainbow', 'overcast', 'sunrise', 'dry', 'tornado', 'sunset', 'humidity', 'cold', 'heat', 'wind', 'cloudy', 'heat wave']

    counter = 0
    while counter <= 100:
        if counter >= 100:
            break
        
        for i in data:
            payload = json.dumps({
            "description": random.choice(status),
            "location": {
                "city": i['capital'],
                "country": i['name'],
            }
            })

            s = requests.Session()
            s.mount(url, HTTPAdapter(max_retries=10))
            req = s.post(url, data=payload)
            print(f'T-{thread} - {req.text}')

        counter += 1    

threads = [Thread(target=main, args=(thread,)) for thread in range(20)]
for thread in threads:
    thread.start()
