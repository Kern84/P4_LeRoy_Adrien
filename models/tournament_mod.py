

TOURNAMENT_DATABASE = []


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

    def prompt_for_tournament(self):
        """Prompt for tournament's infos."""
        name = input("Tournament's name : ")
        start_date = input("Tournament start date (yyyy-mm-dd) : ")
        end_date = input("Tournament end date (yyyy-mm-dd) : ")
        place = input("Place of the tournament : ")
        return name.capitalize(), start_date, end_date, place.capitalize()

    def add_tournament(self):
        """Create a new tournament and add it to the TOURNAMENT_DATABASE."""
        tournament = self.prompt_for_tournament()
        TOURNAMENT_DATABASE.append(tournament)

    def rounds(self, rounds=4):
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



t = Tournament("", "", "")
t.add_tournament()
print(TOURNAMENT_DATABASE)
t.add_tournament()
print(TOURNAMENT_DATABASE)
t.type_of_game()
print(t.type_of_game)

#tourn = Tournament("best of the best", "2021-10-25", "Paris")
#print(tourn)