import requests
import json

if __name__ == '__main__':
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key=DEMO_KEY'
    response = requests.get(url)
    if response.status_code == 200:
#        print(response.content)
        parsed = json.loads(response.text)
        print(json.dumps(parsed, indent=4))
