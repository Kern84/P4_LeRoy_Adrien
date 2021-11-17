TOURNAMENTS_DATABASE = []


class Tournament:
    """A tournament with it's attributes name, start and end date, type of game, number of rounds, players list."""

    def __init__(self, name, place, start_date, end_date, game_type, number_of_rounds=4):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.game_type = game_type
        self.number_of_rounds = number_of_rounds
        tournament = self.name, self.place, self.start_date, self.end_date, self.game_type, self.number_of_rounds
        TOURNAMENTS_DATABASE.append(tournament)

    def serialized(self):
        tournament_infos = {}
        tournament_infos['Name'] = self.name
        tournament_infos['Place'] = self.place
        tournament_infos['Start date'] = self.start_date
        tournament_infos['End date'] = self.end_date
        tournament_infos['Game type'] = self.game_type
        tournament_infos['Number of rounds'] = self.number_of_rounds
        tournament_infos['Remarks'] =
        tournament_infos["Rounds"] =
        return tournament_infos

    def unserialized(self, serialized_tournament):
        name = serialized_tournament['Name']
        place = serialized_tournament['Place']
        start_date = serialized_tournament['Start date']
        end_date = serialized_tournament['End date']
        game_type = serialized_tournament['Game type']
        number_of_rounds = serialized_tournament['Number of rounds']
        remarks = serialized_tournament['Remarks']
        return Tournament(name, place, start_date, end_date, game_type, number_of_rounds, remarks)

    def __repr__(self):
        """Used in print."""
        return f"Tournament's name: {self.name} in {self.place}, from {self.start_date} to {self.end_date}. " \
               f"{self.game_type} games tournament."

    def __str__(self):
        """Used in print."""
        return str(self)
