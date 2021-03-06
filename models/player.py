from tinydb import TinyDB
import json

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

    def serialized(self):
        """Serialize players for the database."""
        player_infos = {}
        player_infos['Firstname'] = self.firstname
        player_infos['Name'] = self.name
        player_infos['Birthdate'] = self.birthdate
        player_infos['Gender'] = self.gender
        player_infos['Elo'] = self.elo
        return player_infos

    def add_players_to_database(self):
        """Save created players to the database."""
        Player.serialized(self)
        players_table = db.table('Players')
        players_table.insert(Player.serialized(self))
        print()
        print("Player added to the database.")

    def elo_update(self):
        """Update players Elo."""
        with open("players_database.json") as f:
            convert_list_player = json.load(f)
            for elements in (convert_list_player["Players"]).items():
                print(elements)
        print()
        player_num = abs(int(input("Enter the player's number you want to modify : ")))
        player = convert_list_player["Players"][str(player_num)]
        print(player)
        print()
        new_elo = abs(int(input("New Elo : ")))
        player["Elo"] = new_elo
        with open("players_database.json", "w") as f:
            json.dump(convert_list_player, f)
            f.seek(0)
            f.write(json.dumps(convert_list_player))
            f.truncate()
        print()
        print("Player's Elo updated.")
