

class Tournament:
    """Class Trounament.
    Has a name, a date, a place, 
    """

    def __init__(self, name, date, place):
        self.name = name
        self.date = date
        self.place = place

    def __str__(self):
        """Used in print."""
        return f"{self.date} - {self.name} tournament, in {self.place}."

    def __repr__(self):
        """Used in print."""
        return str(self)


    def tournament_rounds(self, rounds=4):
        """Number of rounds"""
        self.rounds = rounds

    def type_of_game(self):
        """Blitz, bullet, quick"""
        game_type = input("Choose a type of game : ").capitalize()
        if game_type == "Blitz":
            print("Blitz game = 10 minutes or less per player.")
        if game_type == "Bullet":
            print("Bullet game = 1 minutes per player.")
        if game_type == "Quick":
            print("Quick game = between 10 and 60 minutes per player.")
        return game_type

        