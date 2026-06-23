import requests
import random
import time

while True:

    temperature = round(random.uniform(25, 35), 2)

    data = {
        "temperature": temperature
    }

    response = requests.post(
        "http://127.0.0.1:5000/sensor",
        json=data
    )

    print(response.json())

    time.sleep(5)