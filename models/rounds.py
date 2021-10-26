from tournament import Tournament

class Round:
    """Class Round.
    A round consists of four matches."""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        """Used in print."""
        return f"Round {self.name}"

    def __repr__(self):
        """Used in print."""
        return str(self)

    def round_date_time(self):
        """Automatically saves starting / ending date and time"""
        #prendre le start_date de tournament.py + datetime %H %M
        pass

    def new_round(self):
        pass




round = Round("one")
print(round)