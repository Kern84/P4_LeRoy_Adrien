#from controllers import base

PLAYERS_DATABASE = [('Paul', 'PIERCE', '2020-01-01', 'Male', 1000, 0),
                    ('Lebron', 'JAMES', '2020-01-01', 'Male', 2000, 0),
                    ('Kobe', 'BRYANT', '2020-01-01', 'Male', 2300, 0),
                    ('Mickael', 'JORDAN', '2020-01-01', 'Male', 3000, 0),
                    ('Paula', 'ABDUL', '2020-01-01', 'Female', 800, 0),
                    ('Juju', 'DEFRUIT', '2020-01-01', 'Female', 2100, 0),
                    ('Sophie', 'LAGIRAFE', '2020-01-01', 'Female', 2500, 0),
                    ('Diane', 'LAREINE', '2020-01-01', 'Female', 2800, 0)]

PLAYERS_IN_TOURNAMENT = []

class Player:
    """Class Player.
    Has a name, a firstname, a birthdate, a gender, an elo and a rank.
    """

    def __init__(self, firstname, name, birthdate, gender, elo, rank):
        self.firstname = firstname
        self.name = name
        self.birthdate = birthdate
        self.gender = gender
        self.elo = elo
        self.rank = rank
        player = self.firstname, self.name, self.birthdate, self.gender, self.elo, self.rank
        PLAYERS_IN_TOURNAMENT.append(player)

    def __str__(self):
        """Used in print."""
        return f"{self.name} {self.firstname}, ELO {self.elo}, Rank {self.rank}"

    def __repr__(self):
        """Used in print."""
        return str(self)





            
p = Player()
print(Player)
print()
print(PLAYERS_IN_TOURNAMENT)
