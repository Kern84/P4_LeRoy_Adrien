from models.player import Player

class Match:
    """Class Match."""

    def __init__(self):
        pass

    def match_list(self):
        matchs = []
        matchs.append(Player.player_pairing())
        print(matchs)
