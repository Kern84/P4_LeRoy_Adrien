from models.rounds_matchs import MATCHS


class Views:
    """Class Views.
    Implement the views."""

    def __init__(self):
        pass

    def start_menu(self):
        """Menu at the start of the app."""
        print()
        print("-------------------------------\n"
              "-----Tournament start menu-----\n"
              "-------------------------------")
        print()
        print("Do you want to :\n"
              "1 - Create a new tournament.\n"
              "2 - Consult tournaments in the database.\n"
              "3 - Consult players in the database.\n"
              "4 - Remove a player from database.\n"
              "5 - Exit")

    def add_players_menu(self):
        """Menu for adding players to the tournament."""
        print()
        print("Do you want to :\n"
              "1 - Add players to the tournament from the database.\n"
              "2 - Create new players and add them to the database.\n"
              "3 - Start the tournament.\n"
              "4 - Exit.")

    def rounds_menu(self):
        """Menu for the start of a round."""
        print()
        print("-------------------------------\n"
              "------------New round----------\n"
              "-------------------------------\n")
        print()
        print("Select the round to be played.")

    def matchs_presentation_menu(self):
        """Print that show the matches."""
        x = 1
        y = -4
        for i in range(4):
            print("Match " + str(x))
            print(MATCHS[y])
            x += 1
            y += 1

    def presentation_end_of_matches(self):
        """Print at the end of matches."""
        print("Tournament ranking :")

    def end_tournament(self):
        """Menu for ending the tournament."""
        print()
        print("--------------------------------\n"
              "------End of the tournament-----\n"
              "--------------------------------")
        print()
        print("Do you want to :\n"
              "1 - Update players Elo.\n"
              "2 - Consult players in the database.\n"
              "3 - Consult players of a tournament.\n"
              "4 - Consult tournaments in the database.\n"
              "5 - Consult all the rounds of a tournament.\n"
              "6 - Exit.")

    def short_end_tournament(self):
        print()
        print("Do you want to :\n"
              "1 - Update players Elo.\n"
              "2 - Consult players in the database.\n"
              "3 - Consult players of a tournament.\n"
              "4 - Consult tournaments in the database.\n"
              "5 - Consult all the rounds of a tournament.\n"
              "6 - Exit.")

    def goodbye(self):
        print()
        print("--------------------------------\n"
              "-------------Goodbye------------\n"
              "--------------------------------")
