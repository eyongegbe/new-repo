import requests

class PlayerResourceTests():
    def test_player_request_with_authentication(self):
        uri = "http://api.football-data.org/v2/players/44"
        token = {"X-Auth-Token": "5380111d819c4b0c888404c5b0a8ca2b"}
        response = requests.get(uri,headers=token)
        assert response.status_code == 200

    def test_player_request_without_authentication(self):
        uri = "http://api.football-data.org/v2/players/44"
        response = requests.get(uri)
        assert response.status_code == 200

    def test_get_players_information(self):
        uri = "http://api.football-data.org/v2/players/44"
        token = {"X-Auth-Token": "5380111d819c4b0c888404c5b0a8ca2b"}
        response = requests.get(uri, headers=token)
        actual = response.json()
        player = actual["name"]
        position = actual["position"]
        assert player == "Cristiano Ronaldo"
        assert position == "Attacker"
