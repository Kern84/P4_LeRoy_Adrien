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
        tournament = (self.name, self.place, self.start_date, self.end_date, self.game_type, self.number_of_rounds,
                      self.remarks)
        CURRENT_TOURNAMENT.append(tournament)
        Tournament.current_tournament_for_print(self)

    def current_tournament_for_print(self):
        """Print the current tournament."""
        print()
        print("Tournament :")
        print("Tournament's name: ", str(self.name).strip("(',')"), " in ", str(self.place).strip("(',')"), ", from ",
              str(self.start_date).strip("(',')"), " to ", str(self.end_date).strip("(',')"), ". ",
              str(self.game_type).strip("(',')"), " games tournament. Number of rounds :",
              str(self.number_of_rounds).strip("(',')"), ". Remarks : ", str(self.remarks).strip("(',')"), ".")

    def serialized_tournament(self):
        """Serialize the tournament for the database."""
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

    def save_tournament_database(self):
        """Save tournament info in the database."""
        Tournament.serialized_tournament(self)
        tournament_table = db_tournament.table('Tournaments')
        tournament_table.insert(Tournament.serialized_tournament(self))
        print()
        print("Tournament saved to the database.")
