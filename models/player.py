PLAYERS_DATABASE = []

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
        player = self.firstname, self.name, self.birthdate, self.gender, self.elo
        if player not in PLAYERS_DATABASE:
            PLAYERS_DATABASE.append(player)
        else:
            print("Player already register in the database.")

    def __str__(self):
        """Used in print."""
        return f"Name: {self.name} {self.firstname}, Birthdate: {self.birthdate}, Gender: {self.gender}, ELO: {self.elo}"

    def __repr__(self):
        """Used in print."""
        return str(self)
