from pandas import json_normalize
import requests

def get_CO_list():
    response = requests.get("https://internal-api.mercadolibre.com/shipping/custom-offsets/active")
    info = response.json()
    df = json_normalize(info)
    return df