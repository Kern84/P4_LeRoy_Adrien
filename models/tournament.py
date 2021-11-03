
class Tournaments:
    """initializes a list of tournaments."""

    def __init__(self):
        self.tournaments_list = []

    def create_tournament(self, creation_date, game_type, number_of_rounds):
        a_tournament = Tournament(creation_date, game_type, number_of_rounds)
        self.tournaments_list.append(a_tournament)


class Tournament:
    """A tournament with it's attributes date, type of game, number of rounds, players list."""

    def __init__(self, creation_date, game_type, number_of_rounds):
        self.creation_date = creation_date
        self.game_type = game_type
        self.number_of_rounds = number_of_rounds

"""
class Tour:
    Class Trounament.
    Has a name, a date, a place, 
    

    def __init__(self, name, date, place):
        self.name = name
        self.date = date
        self.place = place

    def __str__(self):
        Used in print
        return f"{self.date} - {self.name} tournament, in {self.place}."

    def __repr__(self):
        Used in print
        return str(self)


    def tournament_rounds(self, rounds=4):
        Number of rounds
        self.rounds = rounds
"""
        