
PLAYERS_DATABASE = []


class Player:
    """Class Player.
    Has a name, a firstname, a birthdate, a gender and an elo.
    """

    def __init__(self, name, firstname, birthdate, gender, elo):
        self.name = name
        self.firstname = firstname
        self.birthdate = birthdate
        self.gender = gender
        self.elo = abs(int(elo))

    def __str__(self):
        """Used in print."""
        return f"{self.name} {self.firstname}, ELO {self.elo} "

    def __repr__(self):
        """Used in print."""
        return str(self)

    def prompt_for_player(self):
        """Prompt for player's infos."""
        firstname = input("Player's firstname : ")
        name = input("Player's name : ")
        birthdate = input("Player's birthdate (yyyy-mm-dd): ")
        gender = input("Player's gender (male / female): ")
        elo = input("Player's rank : ")
        return firstname.capitalize(), name.upper(), birthdate, gender, abs(int(elo))

    def add_players(self):
        """Add a player to the tournament."""
        number_of_players = input("Number of players : ")
        for i in range(abs(int(number_of_players))):
            players = self.prompt_for_player()
            PLAYERS_DATABASE.append(players)
            
    def game_results(self, victories=0, draws=0, losses=0):
        """Player's results."""
        self.victories = victories
        self.draws = draws
        self.losses = losses

    def player_pairing(self):
        """Pairing the players."""
        if round == first_round:
            top_tier = sorted(PLAYERS_DATABASE, key=lambda rank: rank[4], reverse=True)[:4]
            low_tier = sorted(PLAYERS_DATABASE, key=lambda rank: rank[4], reverse=True)[4:]
            print(top_tier)
            print(low_tier)
        else:
            pass

    def player_rank(self):
        """Determine by victories, draws and losses during a tournament"""
        pass


p = Player("", "", "", "", "0")
# John = Player("Margoulin", "John", "24 Juin 1990", "M", "-1200")

p.add_players()
print(PLAYERS_DATABASE)
p.player_pairing()

#print(John)

