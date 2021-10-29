from datetime import datetime


class Round:
    """Class Round.
    A round consists of four matches."""

    def __init__(self, name):
        self.name = name

    def round_date_time(self):
        """Automatically saves starting / ending date and time"""
        now = datetime.now()
        time_now = now.strftime("%Y-%m-%d, %H:%M:%S")
        return time_now

    def matchs_per_round(self):
        round1 = MATCHS[:4]
        round2 = MATCHS[4:8]
        round3 = MATCHS[8:12]
        round4 = MATCHS[12:]
        matchs_round = round1, round2, round3, round4
        ROUNDS.append(matchs_round)


class Match:
    """Class Match."""

    def __init__(self):
        pass
