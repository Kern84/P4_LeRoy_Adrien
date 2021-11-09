PLAYERS_DATABASE = [('PIERCE', 'Paul', "2020-11-08", "Male", 1000),
                    ('ABDUL', 'Paula', "2020-11-08", "Female", 2000),
                    ('LAGIRAFE', 'Sophie', "2020-11-08", "Female", 1200),
                    ('DEFRUIT', 'Juju', "2020-11-08", "Female", 800),
                    ('BRYANT', 'Kobe', "2020-11-08", "Male", 3000),
                    ('JAMES', 'Lebron', "2020-11-08", "Male", 2300),
                    ('JORDAN', 'Mickael', '2020-11-08', 'Male', 3100),
                    ('LAREINE', 'Diane', '2021-11-08', 'Female', 3200)]

PLAYERS_IN_TOURNAMENT = []


class Player:
    """Class Player.
    Has a name, a firstname, a birthdate, a gender and an elo.
    """

    def __init__(self, firstname="Firstname", name="NAME", birthdate="Birthdate", gender="Gender", elo=0):
        self.firstname = firstname
        self.name = name
        self.birthdate = birthdate
        self.gender = gender
        self.elo = elo
        player = self.name, self.firstname, self.birthdate, self.gender, self.elo
        if player not in PLAYERS_DATABASE:
            PLAYERS_IN_TOURNAMENT.append(player)
            PLAYERS_DATABASE.append(player)
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
