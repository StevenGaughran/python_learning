# ~~~~ This handles the API request. ~~~~
import requests


response = requests.get("https://api.opendota.com/api/heroStats")
response.raise_for_status()
stats = response.json()


