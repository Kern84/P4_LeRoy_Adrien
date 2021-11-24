from tinydb import TinyDB

PLAYERS_IN_TOURNAMENT = []

ROUNDS = []

CURRENT_TOURNAMENT = []

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
        tournament = self.name, self.place, self.start_date, self.end_date, self.game_type, self.number_of_rounds, self.remarks
        CURRENT_TOURNAMENT.append(tournament)
        Tournament.current_tournament_for_print(self)

    def current_tournament_for_print(self):
        current_tournament_for_print = f"Tournament's name: {self.name} in {self.place}, from {self.start_date} to {self.end_date}. " \
                                       f"{self.game_type} games tournament. Remarks : {self.remarks}."
        print()
        print("Tournament :")
        print(current_tournament_for_print)

    def serialized_tournament(self):
        tournament_infos = {}
        tournament_infos['Name'] = CURRENT_TOURNAMENT[0][0]
        tournament_infos['Place'] = CURRENT_TOURNAMENT[0][1]
        tournament_infos['Start date'] = CURRENT_TOURNAMENT[0][2]
        tournament_infos['End date'] = CURRENT_TOURNAMENT[0][3]
        tournament_infos['Game type'] = CURRENT_TOURNAMENT[0][4]
        tournament_infos['Number of rounds'] = CURRENT_TOURNAMENT[0][5]
        tournament_infos['Remarks'] = CURRENT_TOURNAMENT[0][6]
        tournament_infos['Players in tournament'] = PLAYERS_IN_TOURNAMENT
        tournament_infos['Rounds list'] = ROUNDS
        return tournament_infos

    def serialized(self):
        tournament_infos = {}
        tournament_infos['Name'] = self.name
        tournament_infos['Place'] = self.place
        tournament_infos['Start date'] = self.start_date
        tournament_infos['End date'] = self.end_date
        tournament_infos['Game type'] = self.game_type
        tournament_infos['Number of rounds'] = self.number_of_rounds
        tournament_infos['Remarks'] = self.remarks
        tournament_infos['Players in tournament'] = PLAYERS_IN_TOURNAMENT
        tournament_infos['Rounds list'] = ROUNDS
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
        """Save tournament info in the database."""
        Tournament.serialized_tournament(self)
        tournament_table = db_tournament.table('Tournaments')
        tournament_table.insert(Tournament.serialized_tournament(self))
        print()
        print("Tournament saved to the database.")
