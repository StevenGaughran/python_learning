# ~~~~ This handles the API request. ~~~~
import requests


# ~~~~ STATS ~~~~
def stats():
    response = requests.get("https://api.opendota.com/api/heroStats")
    response.raise_for_status()
    return response.json()


# ~~~~ MATCHUPS ~~~~
def matchups():
    response = requests.get("https://api.opendota.com/api/heroes/2/matchups")
    response.raise_for_status()
    return response.json()
