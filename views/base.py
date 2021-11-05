from models.rounds_matchs import Match, MATCHS


class Views:
    """Class Views.
    Implement the views."""

    def __init__(self):
        pass

    def start_menu(self):
        print()
        print("-------------------------------\n"
              "-----Tournament start menu-----\n"
              "-------------------------------")
        print()
        print("Do you want to :\n"
              "1 - Create a new tournament.\n"
              "2 - Consult the tournaments in the database.\n"
              "3 - Consult the players in the database.\n"
              "4 - Exit")

    def add_players_menu(self):
        print()
        print("Do you want to :\n"
              "1 - Add players to the tournament from the database.\n"
              "2 - Create new players and add them to the tournament.\n"
              "3 - Exit.")

    def rounds_menu(self):
        print()
        print("-------------------------------\n"
              "------------New round----------\n"
              "-------------------------------\n")
        print()
        print("Select the round to be played.")

    def matchs_presentation_menu(self):
        print()
        x = 1
        for i in MATCHS:
            print("Match" + str(x))
            print(i)
            x += 1
