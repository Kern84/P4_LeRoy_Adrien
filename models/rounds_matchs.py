from datetime import datetime

from models.player import Player


#from tournament import Tournament

class Round:
    """Class Round.
    A round consists of four matches."""

    def __init__(self, name):
        self.name = name

    def prompt_for_round_name(self):
        name = input("Round's name (one, two, ...) : ")
        round_name = "Round " + name.lower()
        return round_name

    def round_date_time(self):
        """Automatically saves starting / ending date and time"""
        now = datetime.now()
        time_now = now.strftime("%Y-%m-%d, %H:%M:%S")
        return time_now

    def new_round(self):
        pass


class Match:
    """Class Match."""

    def __init__(self):
        pass

    def match_list(self):
        matchs = []
        matchs.append(Player.player_pairing())
        print(matchs)


round = Round("")
#round.prompt_for_round_name()
#print(round.prompt_for_round_name())

