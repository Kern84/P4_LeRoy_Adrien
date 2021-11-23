from tinydb import TinyDB

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
        Player.add_players_to_database(self)

    def __str__(self):
        """Used in print."""
        return f"Name: {self.name} {self.firstname}, Birthdate: {self.birthdate}, Gender: {self.gender}, ELO: {self.elo}"

    def __repr__(self):
        """Used in print."""
        return str(self)

    def serialized(self):
        player_infos = {}
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

    def add_players_to_database(self):
        Player.serialized(self)
        players_table = db.table('Players')
        players_table.insert(Player.serialized(self))
        print()
        print("Player added to the database.")
