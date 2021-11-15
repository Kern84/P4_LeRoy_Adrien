from datetime import datetime

MATCHS = []

ROUNDS = []


class Round:
    """Class Round.
    A round consists of four matches."""

    def __init__(self, round="Round"):
        self.round = round
        ROUNDS.append(self.round)

    def round_date_time(self):
        """Automatically saves starting / ending date and time"""
        now = datetime.now()
        time_now = now.strftime("%Y-%m-%d, %H:%M:%S")
        return time_now


class Match:
    """Class Match."""

    def __init__(self, match1, match2, match3, match4):
        self.match1 = match1
        self.match2 = match2
        self.match3 = match3
        self.match4 = match4
        MATCHS.append(self.match1)
        MATCHS.append(self.match2)
        MATCHS.append(self.match3)
        MATCHS.append(self.match4)
        Match.match_to_round(self)

    def match_to_round(self):
        match_round = MATCHS[:4]
        return Round(match_round)
