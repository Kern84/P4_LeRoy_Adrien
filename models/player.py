from tinydb import TinyDB

PLAYERS_DATABASE = [('PIERCE', 'Paul', "2020-11-08", "Male", 1000),
                    ('ABDUL', 'Paula', "2020-11-08", "Female", 2000),
                    ('LAGIRAFE', 'Sophie', "2020-11-08", "Female", 1200),
                    ('DEFRUIT', 'Juju', "2020-11-08", "Female", 800),
                    ('BRYANT', 'Kobe', "2020-11-08", "Male", 3000),
                    ('JAMES', 'Lebron', "2020-11-08", "Male", 2300),
                    ('JORDAN', 'Mickael', '2020-11-08', 'Male', 3100),
                    ('LAREINE', 'Diane', '2021-11-08', 'Female', 3200)]

PLAYERS_IN_TOURNAMENT = []

player_infos = {}

db = TinyDB("players_database.json")


class Player:
    """Class Player.
    Has a name, a firstname, a birthdate, a gender and an elo.
    """

    def __init__(self, firstname, name, birthdate, gender, elo):
        self.firstname = firstname
        self.name = name
        self.birthdate = birthdate
        self.gender = gender
        self.elo = elo
        player = self.name, self.firstname, self.birthdate, self.gender, self.elo
        Player.serialized(self)
        if player not in db:
            PLAYERS_IN_TOURNAMENT.append(player)
            self.save_players_database()
            print()
            print("Player added to the tournament and the database.")
        else:
            print()
            print("Player already register in the database.")

    def __str__(self):
        """Used in print."""
        return f"Name: {self.name} {self.firstname}, Birthdate: {self.birthdate}, Gender: {self.gender}, ELO: {self.elo}"

    def __repr__(self):
        """Used in print."""
        return str(self)

    def serialized(self):
        player_infos['Firstname'] = self.firstname
        player_infos['Name'] = self.name
        player_infos['Birthdate'] = self.birthdate
        player_infos['Gender'] = self.gender
        player_infos['Elo'] = self.elo
        return player_infos

    def deserialized(self, serialized_player):
        firstname = serialized_player["Firstname"]
        name = serialized_player["Name"]
        birthdate = serialized_player["Birthdate"]
        gender = serialized_player["Gender"]
        elo = serialized_player["Elo"]
        return Player(name, firstname, birthdate, gender, elo)

    def save_players_database(self):
        players_table = db.table('Players')
        players_table.insert(player_infos)
