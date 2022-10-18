import requests
import time

for iter, _ in enumerate(range(50000)):
    x = requests.get('https://gtresume.com')
    print(f"{iter}: {x.status_code}")
    time.sleep(.1)