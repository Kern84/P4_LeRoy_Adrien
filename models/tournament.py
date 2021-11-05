class Tournaments:
    """initializes a list of tournaments."""

    def __init__(self):
        self.tournaments_list = []

    def create_tournament(self, name, place, start_date, end_date, game_type, number_of_rounds):
        a_tournament = Tournament(name, place, start_date, end_date, game_type, number_of_rounds)
        self.tournaments_list.append(a_tournament)


class Tournament:
    """A tournament with it's attributes name, start and end date, type of game, number of rounds, players list."""

    def __init__(self, name="Name", place="Place", start_date="Start date", end_date="End date",
                 game_type="Game type", number_of_rounds="Number of rounds"):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.game_type = game_type
        self.number_of_rounds = number_of_rounds
        self.players_database = []
        self.rounds_list = []

    def __repr__(self):
        """Used in print."""
        return f"Tournament's name: {self.name} in {self.place}, from {self.start_date} to {self.end_date}. " \
               f"{self.game_type} games tournament."

    def __str__(self):
        """Used in print."""
        return str(self)
