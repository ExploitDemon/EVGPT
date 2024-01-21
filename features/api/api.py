import json


def get_data(session):
    team_id = "544835"
    url = f"https://metabet.static.api.areyouwatchingthis.com/api/odds.json?q={team_id}&apiKey=219f64094f67ed781035f5f7a08840fc"
    response = session.get(url)
    response.raise_for_status()
    return json.loads(response.text)
