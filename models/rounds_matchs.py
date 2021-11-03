
from datetime import datetime


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

    def __init__(self):
        self.matchs = []

