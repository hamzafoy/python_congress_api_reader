import requests
import os
import dotenv
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get('API_KEY')
url = "https://api.congress.gov/v3/bill?api_key="+str(api_key)+"&format=json"

request = requests.get(url).json()
for i in range(3):
    print(request['bills'][i])