from tinydb import TinyDB

tournament_infos = {}
db_tournament = TinyDB("tournament_database.json")


class Tournament:
    """A tournament with it's attributes name, place, start and end date, type of game, number of rounds."""

    def __init__(self, name, place, start_date, end_date, game_type, number_of_rounds=4, remarks=None):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.game_type = game_type
        self.number_of_rounds = number_of_rounds
        self.remarks = remarks
        Tournament.serialized(self)
        Tournament.deserialized(self)
        self.save_tournament_database()

    def serialized(self):
        tournament_infos['Name'] = self.name
        tournament_infos['Place'] = self.place
        tournament_infos['Start date'] = self.start_date
        tournament_infos['End date'] = self.end_date
        tournament_infos['Game type'] = self.game_type
        tournament_infos['Number of rounds'] = self.number_of_rounds
        tournament_infos['Remarks'] = self.remarks
        return tournament_infos

    def deserialized(self, serialized_tournament):
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

    def save_tournament_database(self):
        tournament_table = db_tournament.table("Tournaments")
        tournament_table.insert(tournament_infos)
