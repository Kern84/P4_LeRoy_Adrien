#from controllers.base import PLAYERS_DATABASE

PLAYERS_DATABASE = [('Paul', 'PIERCE', '2000-01-02', 'Male', 1000, 0.0),
                    ('Zaza', 'PATCHOULIA', '2000-01-02  ', 'Male', 2000, 0.0),
                    ('Kobe', 'BRYANT', '2000-01-02  ', 'Male', 3000, 0.0),
                    ('Lebron', 'JAMES', '2000-01-02  ', 'Male', 1200, 0.0),
                    ('Juju', 'ZEN', '2000-01-02  ', 'Female', 800, 0.0),
                    ('Sophie', 'LAGIRAFE', '2000-01-02  ', 'Female', 1200, 0.0),
                    ('Diane', 'LAREINE', '2000-01-02  ', 'Female', 2800, 0.0),
                    ('Paula', 'ABDUL', '2000-01-02  ', 'Female', 2300, 0.0)]

PLAYER_DICT = {}

class Player:
    """Class Player.
    Has a name, a firstname, a birthdate, a gender, an elo and a rank.
    """

    def __init__(self, name, firstname, birthdate, gender, elo, rank):
        self.name = name
        self.firstname = firstname
        self.birthdate = birthdate
        self.gender = gender
        self.elo = elo
        self.rank = rank

    def __str__(self):
        """Used in print."""
        return f"{self.name} {self.firstname}, ELO {self.elo}, Rank {self.rank}"

    def __repr__(self):
        """Used in print."""
        return str(self)

    def player_name(self):
        for i, val in enumerate(PLAYERS_DATABASE):
            player_index = "player " + str(i+1)
            player_info = str(PLAYERS_DATABASE[i])
            print(player_index, player_info)
            PLAYER_DICT[player_index] = player_info
            

p = Player("", "","", "", 0, 0)
p.player_name()
print(PLAYER_DICT)