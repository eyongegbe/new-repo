import requests

class matchesResourcesTests():
    def test_get_matches(self):
        uri = "https://api.football-data.org/v2/matches/233445"
        token = {"X-Auth-Token": "5380111d819c4b0c888404c5b0a8ca2b"}
        response = requests.get(uri, headers=token)
        print(response.text)
        assert response.status_code == 403

