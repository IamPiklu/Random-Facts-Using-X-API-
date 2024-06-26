import requests

def get_fact():
    api_url = 'https://api.api-ninjas.com/v1/facts'
    response = requests.get(api_url, headers={'X-Api-Key': 'api-ninjas Key'})
    if response.status_code == requests.codes.ok:
        fact = response.json()[0]['fact']  # Extract the fact from the response
        return fact
    else:
        print("Error:", response.status_code, response.text)
        return None
