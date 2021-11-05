from datetime import datetime

MATCHS = []


class Round:
    """Class Round.
    A round consists of four matches."""

    def __init__(self, name):
        self.name = name
        self.rounds = []

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
        matchs = self.match1, self.match2, self.match3, self.match4
        MATCHS.append(matchs)
