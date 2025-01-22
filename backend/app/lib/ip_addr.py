import requests
import os
from dotenv import load_dotenv
load_dotenv()
key = os.getenv("IPSTACK_API_KEY","")
def get_ip_info(ip):
    url = f"http://api.ipstack.com/{ip}?access_key={key}"
    response = requests.get(url)
    data = response.json()

    return {
        'city': data.get('city', ''),
        'country': data.get('country_name', ''),
        'zip': data.get('zip', ''),
        'type': data.get('type', '')
    }