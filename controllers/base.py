import sys
from datetime import datetime
import json

from models.player import Player
from models.tournament import Tournament, PLAYERS_IN_TOURNAMENT, ROUNDS, CURRENT_TOURNAMENT
from models.rounds_matchs import Match, Round, MATCHS

from views.base import Views

RANKING = []
LIST_RANK = []
ROUND_INFOS = []


class Controller:
    """Class Controller.
    Define the tournament controller"""

    def start_menu_tournament(self):
        """Start menu for the tournament. 1 = create tournament; 2 = consult previous tournaments;
            3 = consult players in database; 4 = remove a player from the database; 5 = exit."""
        try:
            menu_choice = abs(int(input("Enter the menu number : ")))
            if menu_choice == 1:
                Controller.prompt_for_create_tournament(self)
                print()
                Views.add_players_menu(self)
                Controller.choice_for_add_players_menu(self)
            if menu_choice == 2:
                try:
                    with open("tournament_database.json") as f:
                        convert_list_tournament = json.load(f)
                    print()
                    print("Tournaments :")
                    for i in range(len(convert_list_tournament["Tournaments"])):
                        print(convert_list_tournament["Tournaments"][str(i + 1)])
                except json.decoder.JSONDecodeError:
                    print()
                    print("No previous tournaments saved.")
                Views.start_menu(self)
                Controller.start_menu_tournament(self)
            if menu_choice == 3:
                try:
                    with open("players_database.json") as f:
                        convert_list_player = json.load(f)
                        print()
                        print("Players (sorted by names):")
                        result = sorted(convert_list_player["Players"].items(), key=lambda x: x[1]["Name"])
                        for item in result:
                            print(item)
                except json.decoder.JSONDecodeError:
                    print()
                    print("No players saved in the database.")
                Views.start_menu(self)
                Controller.start_menu_tournament(self)
            if menu_choice == 4:
                print()
                with open("players_database.json") as f:
                    convert_list_players = json.load(f)
                for elements in (convert_list_players["Players"]).items():
                    print(elements)
                print()
                player_remove = abs(int(input("Enter the player's number you want to remove from the database : ")))
                del convert_list_players["Players"][str(player_remove)]
                with open("players_database.json", "w") as f:
                    json.dump(convert_list_players, f)
                print("The player as been remove from the database.")
                Views.start_menu(self)
                Controller.start_menu_tournament(self)
            if menu_choice == 5:
                Views.goodbye(self)
                sys.exit()
        except ValueError:
            print("You must enter a valid number.")
            Views.start_menu(self)
            Controller.start_menu_tournament(self)

    def prompt_for_create_tournament(self):
        """Prompt for tournament's info."""
        try:
            name = input("Tournament's name : ").capitalize(),
            place = input("Place of the tournament : ").capitalize(),
            start_date = input("Tournament start date (yyyy-mm-dd) : "),
            end_date = input("Tournament end date (yyyy-mm-dd) : "),
            game_type = input("Tournament type of game (Blitz, Bullet, Quick): ").capitalize(),
            number_of_rounds = abs(int(input("Number of rounds in the tournament : ")))
            remarks = input("Remarks about the tournament : ").capitalize()
            Tournament(name, place, start_date, end_date, game_type, number_of_rounds, remarks)
        except ValueError:
            print("You must enter a correct value.")
            Controller.prompt_for_create_tournament(self)

    def tournament_execution(self):
        """Tournament path."""
        for rounds in range(CURRENT_TOURNAMENT[0][5]):
            Views.rounds_menu(self)
            Controller.round_affector(self)
            Views.matchs_presentation_menu(self)
            Controller.end_of_matches(self)
            Controller.closing_of_round(self)
        Tournament.save_tournament_database(self)
        Controller.tournament_winner(self)
        Views.end_tournament(self)
        Controller.end_of_tournament(self)

    def choice_for_add_players_menu(self):
        """Menu to add players to the tournament.
        1 = add players from database; 2 = Create players; 3 = Start the tournament; 4 = exit."""
        try:
            menu_choice = abs(int(input("Enter the menu number : ")))
            print()
            if menu_choice == 1:
                with open("players_database.json") as f:
                    convert_list_players = json.load(f)
                if not convert_list_players:
                    print()
                    print("No players saved in the database.")
                else:
                    Controller.add_players_tournament(self)
                Views.add_players_menu(self)
                Controller.choice_for_add_players_menu(self)
            if menu_choice == 2:
                number_of_players_to_add = abs(int(input("Number of players to add : ")))
                print()
                for i in range(number_of_players_to_add):
                    print("Player " + str(i + 1))
                    Controller.create_player(self)
                Views.add_players_menu(self)
                Controller.choice_for_add_players_menu(self)
            if menu_choice == 3:
                Controller.checking_number_of_players(self)
            if menu_choice == 4:
                Views.goodbye(self)
                sys.exit()
        except ValueError:
            print("You must enter a valid number.")
            Views.add_players_menu(self)
            Controller.choice_for_add_players_menu(self)

    def create_player(self):
        """Create players for database and tournament. Prompt for players info."""
        try:
            firstname = input("Player's firstname : ").capitalize()
            name = input("Player's name : ").upper()
            birthdate = input("Player's birthdate (yyyy-mm-dd): ")
            gender = input("Player's gender (male / female): ").capitalize()
            elo = abs(int(input("Player's elo : ")))
            Player(firstname, name, birthdate, gender, elo)
        except ValueError:
            print("You must enter a valid number.")
            Views.add_players_menu(self)
            Controller.choice_for_add_players_menu(self)

    def add_players_tournament(self):
        """Add players who are already in the players database."""
        PLAYERS_IN_TOURNAMENT.clear()
        try:
            players_to_add = abs(int(input("Number of database players to add to the tournament : ")))
            print()
            with open("players_database.json") as f:
                convert_list_players = json.load(f)
            for elements in (convert_list_players["Players"]).items():
                print(elements)
            print()
            x = 0
            while x in range(players_to_add):
                player_num = abs(int(input("Enter the player's number to add to the tournament : ")))
                player = convert_list_players["Players"][str(player_num)]
                player_str = player["Firstname"], player["Name"], player["Elo"]
                PLAYERS_IN_TOURNAMENT.append(player_str)
                print("Player added to the tournament.")
                print()
                x += 1
        except KeyError:
            print("Youn must enter a valid number.")
            Controller.add_players_tournament(self)
        print()

    def checking_number_of_players(self):
        """Checking if the number of players in the tournament equal 8."""
        if len(PLAYERS_IN_TOURNAMENT) == 8:
            print()
            print("The tournament is full.")
            print()
            print("Players in the tournament :")
            for item in PLAYERS_IN_TOURNAMENT:
                print(item)
        if len(PLAYERS_IN_TOURNAMENT) > 8:
            print()
            print("The tournament must consists of height players. Please remove players.")
            for index in enumerate(PLAYERS_IN_TOURNAMENT):
                print(index)
            player_to_remove = abs(int(input("Enter the player's number to remove from the tournament : ")))
            del PLAYERS_IN_TOURNAMENT[player_to_remove]
            Controller.checking_number_of_players(self)
        if len(PLAYERS_IN_TOURNAMENT) < 8:
            print()
            print("Not enough players in the tournament. Please add some.")
            Views.add_players_menu(self)
            Controller.choice_for_add_players_menu(self)

    def round_date_time(self):
        """Automatically saves starting / ending date and time"""
        now = datetime.now()
        time_now = now.strftime("%Y-%m-%d, %H:%M:%S")
        return time_now

    def prompt_for_round_name(self):
        """Prompt for registering the number of the round."""
        possible_round = ["one", "two", "three", "four", "five", "six", "seven", "height", "nine", "ten"]
        valid_name = False
        while not valid_name:
            name = input("Round (one, two, ...) : ").lower()
            round_name = "Round " + name
            if name in possible_round:
                valid_name = True
                return round_name
            else:
                print()
                print("You must enter a valid input.\n"
                      "Round name :")

    def save_round_name_and_start_time(self):
        """Save the round name and start time for models/Round."""
        round_name = Controller.prompt_for_round_name(self)
        start_time = Controller.round_date_time(self)
        print()
        print(round_name)
        print(start_time)
        print()
        ROUND_INFOS.append(round_name)
        ROUND_INFOS.append(start_time)

    def round_affector(self):
        """variable for choosing the round."""
        Controller.save_round_name_and_start_time(self)
        round_name = ROUND_INFOS[-2]
        if round_name == "Round one":
            Controller.pairing_players_round_one(self)
        else:
            Controller.pairing_players_other_rounds(self)

    def pairing_players_round_one(self):
        """Pairing players for the first round."""
        top_tier_elo = sorted(PLAYERS_IN_TOURNAMENT, key=lambda elo: elo[2], reverse=True)[:4]
        low_tier_elo = sorted(PLAYERS_IN_TOURNAMENT, key=lambda elo: elo[2], reverse=True)[4:]
        for i in range(4):
            player_1 = top_tier_elo[i]
            score_1 = 0,
            player_2 = low_tier_elo[i]
            score_2 = 0,
            Match(player_1, score_1, player_2, score_2)

    def pairing_players_other_rounds(self):
        """Pairing players for all rounds except the first round."""
        for i in range(4):
            z = 1
            match = RANKING[0], RANKING[z]
            match_verify = RANKING[z], RANKING[0]
            try:
                if match not in MATCHS and match_verify not in MATCHS:
                    player1 = RANKING[0][0], RANKING[0][1], RANKING[0][2]
                    player2 = RANKING[z][0], RANKING[z][1], RANKING[z][2]
                    Match(player1, (RANKING[0][3],), player2, (RANKING[z][3],))
                    del RANKING[:2]
                else:
                    print("The match {} VS {} as already been played.".format(RANKING[0], RANKING[z]))
                    z += 1
                    for n in range(len(RANKING)):
                        match = RANKING[0], RANKING[z]
                        match_verify = RANKING[z], RANKING[0]
                        if match not in MATCHS and match_verify not in MATCHS:
                            player1 = RANKING[0][0], RANKING[0][1], RANKING[0][2]
                            player2 = RANKING[z][0], RANKING[z][1], RANKING[z][2]
                            Match(player1, (RANKING[0][3],), player2, (RANKING[z][1],))
                            del RANKING[z]
                            del RANKING[0]
                            break
                        else:
                            z += 1
            except IndexError:
                pass

    def end_of_matches(self):
        """Prompt to validate the end of matches."""
        print()
        end = input("Enter 'OK' to continue when matches are done : ").upper()
        if end == "OK":
            print()
            if len(MATCHS) <= 4:
                Controller.match_results_round_one(self)
            else:
                Controller.match_results_others(self)
            print()
        else:
            print("press 'OK' to continue...")
            Controller.end_of_matches(self)
            print()

    def match_results_round_one(self):
        """Match results round one."""
        alt_match = []
        possible_results = ["win", "draw", "lost"]
        win = 1
        draw = 0.5
        lost = 0
        y = 1
        for i in range(4):
            print("Match " + str(y))
            print(MATCHS[i][0], "  VS  ", MATCHS[i][1])
            print()
            print(MATCHS[i][0])
            valid_result = False
            while not valid_result:
                result = input("Player result (win, draw, lost): ").lower()
                if result in possible_results:
                    if result == "win":
                        p1 = MATCHS[i][0][3] + win
                        p2 = MATCHS[i][1][3] + lost
                        match = MATCHS[i][0][:3] + (p1,), MATCHS[i][1][:3] + (p2,)
                        alt_match.append(match)
                        print(alt_match)
                        print("Then {} {} lost.".format(MATCHS[i][1][0], MATCHS[i][1][1]))
                    if result == "draw":
                        p1 = MATCHS[i][0][3] + draw
                        p2 = MATCHS[i][1][3] + draw
                        match = MATCHS[i][0][:3] + (p1,), MATCHS[i][1][:3] + (p2,)
                        alt_match.append(match)
                        print("Then {} {} also draw.".format(MATCHS[i][1][0], MATCHS[i][1][1]))
                    if result == "lost":
                        p1 = MATCHS[i][0][3] + lost
                        p2 = MATCHS[i][1][3] + win
                        match = MATCHS[i][0][:3] + (p1,), MATCHS[i][1][:3] + (p2,)
                        alt_match.append(match)
                        print("Then {} {} win.".format(MATCHS[i][1][0], MATCHS[i][1][1]))
                    valid_result = True
                else:
                    print("You must enter a valid input.")
                    print()
            print()
            print(alt_match[i][0][0], alt_match[i][0][1], "Score :", alt_match[i][0][3])
            print(alt_match[i][1][0], alt_match[i][1][1], "Score :", alt_match[i][1][3])
            y += 1
            print()
        MATCHS.clear()
        for element in alt_match:
            MATCHS.append(element)
        Views.presentation_end_of_matches(self)
        Controller.end_of_round_one(self)

    def match_results_others(self):
        """Match results other rounds."""
        alt_match = []
        possible_results = ["win", "draw", "lost"]
        win = 1
        draw = 0.5
        lost = 0
        y = 1
        z = 0
        for i in range(-4, 0):
            print("Match " + str(y))
            print(MATCHS[i][0], "  VS  ", MATCHS[i][1])
            print()
            print(MATCHS[i][0])
            valid_result = False
            while not valid_result:
                result = input("Player result (win, draw, lost): ").lower()
                if result in possible_results:
                    if result == "win":
                        p1 = MATCHS[i][0][3] + win
                        p2 = MATCHS[i][1][3] + lost
                        match = MATCHS[i][0][:3] + (p1,), MATCHS[i][1][:3] + (p2,)
                        alt_match.append(match)
                        print(alt_match)
                        print("Then {} {} lost.".format(MATCHS[i][1][0], MATCHS[i][1][1]))
                    if result == "draw":
                        p1 = MATCHS[i][0][3] + draw
                        p2 = MATCHS[i][1][3] + draw
                        match = MATCHS[i][0][:3] + (p1,), MATCHS[i][1][:3] + (p2,)
                        alt_match.append(match)
                        print("Then {} {} also draw.".format(MATCHS[i][1][0], MATCHS[i][1][1]))
                    if result == "lost":
                        p1 = MATCHS[i][0][3] + lost
                        p2 = MATCHS[i][1][3] + win
                        match = MATCHS[i][0][:3] + (p1,), MATCHS[i][1][:3] + (p2,)
                        alt_match.append(match)
                        print("Then {} {} win.".format(MATCHS[i][1][0], MATCHS[i][1][1]))
                    valid_result = True
            else:
                print("You must enter a valid input.")
                print()
            print()
            print(alt_match[z][0][0], alt_match[z][0][1], "Score :", alt_match[z][0][3])
            print(alt_match[z][1][0], alt_match[z][1][1], "Score :", alt_match[z][1][3])
            y += 1
            z += 1
            print()
        del MATCHS[-4:]
        for element in alt_match:
            MATCHS.append(element)
        Views.presentation_end_of_matches(self)
        Controller.end_of_other_rounds(self)

    def end_of_round_one(self):
        """At the end of matches round one. RANKING display."""
        for i in range(4):
            LIST_RANK.append(MATCHS[i][0])
            LIST_RANK.append(MATCHS[i][1])
        for elements in sorted(LIST_RANK, key=lambda a: (a[3], a[2]), reverse=True):
            RANKING.append(elements)
        for elements in enumerate(RANKING, start=1):
            print(elements)

    def end_of_other_rounds(self):
        """At the end of matches round two and above. RANKING display."""
        LIST_RANK.clear()
        RANKING.clear()
        for i in range(-4, 0):
            LIST_RANK.append(MATCHS[i][0])
            LIST_RANK.append(MATCHS[i][1])
        for elements in sorted(LIST_RANK, key=lambda a: (a[3], a[2]), reverse=True):
            RANKING.append(elements)
        for elements in enumerate(RANKING, start=1):
            print(elements)

    def closing_of_round(self):
        """Prompt for validate the end of the round."""
        choice = input("Closing this round ? (yes / no) : ").lower()
        if choice == "yes":
            end_time = Controller.round_date_time(self)
            print()
            print(end_time)
            Round(ROUND_INFOS[-2], ROUND_INFOS[-1], end_time)
            print()
            print(ROUNDS[-1])
        else:
            print()
            print("You must enter 'yes' or 'no'.")
            Controller.closing_of_round(self)

    def end_of_tournament(self):
        """At the end of the tournament.
        1- update player elo; 2- Consult players in database; 3- Consult players of a tournament;
        4- Consult tournaments in database; 5- Consult rounds of a tournament; 6- Exit."""
        try:
            choice = abs(int(input("Enter the menu number : ")))
            print()
            if choice == 1:
                Player.elo_update(self)
                print()
                Views.short_end_tournament(self)
                Controller.end_of_tournament(self)
            if choice == 2:
                with open("players_database.json") as f:
                    convert_list_player = json.load(f)
                print("Players in the database :")
                for element in (convert_list_player["Players"]).items():
                    print(element)
                print()
                Views.short_end_tournament(self)
                Controller.end_of_tournament(self)
            if choice == 3:
                Controller.tournament_players(self)
                print()
                Views.short_end_tournament(self)
                Controller.end_of_tournament(self)
            if choice == 4:
                with open("tournament_database.json") as f:
                    convert_list_tournament = json.load(f)
                print("Tournaments in the database :")
                for element in (convert_list_tournament["Tournaments"]).items():
                    print(element)
                print()
                Views.short_end_tournament(self)
                Controller.end_of_tournament(self)
            if choice == 5:
                Controller.rounds_in_tournament(self)
                print()
                Views.short_end_tournament(self)
                Controller.end_of_tournament(self)
            if choice == 6:
                Views.goodbye(self)
                sys.exit()
        except ValueError:
            print()
            print("You must enter a valid number.")
            print()
            Views.end_tournament(self)
            Controller.end_of_tournament(self)

    def tournament_players(self):
        """Consult players in a tournament."""
        with open("tournament_database.json") as f:
            convert_list_tournament = json.load(f)
        for element in (convert_list_tournament["Tournaments"]).items():
            print(element)
        print()
        try:
            tournament_num = abs(
                int(input("Enter the tournament number for which you can consult the list of players : ")))
            players_tournament = convert_list_tournament["Tournaments"][str(tournament_num)]
            print()
            print("Players in the tournament :")
            for elements in players_tournament["Players in tournament"]:
                print(elements)
        except ValueError:
            print()
            print("You must enter a valid number.")
            Controller.tournament_players(self)
        print()

    def rounds_in_tournament(self):
        """Consult rounds and matches of a tournament."""
        with open("tournament_database.json") as f:
            convert_list_tournament = json.load(f)
        for element in (convert_list_tournament["Tournaments"]).items():
            print(element)
        print()
        try:
            rounds_in_tournament = abs(
                int(input("Enter the tournament number for which you can consult the list of rounds : ")))
            rounds_tournament = convert_list_tournament["Tournaments"][str(rounds_in_tournament)]
            print()
            print("Rounds in a tournament :")
            for elements in rounds_tournament["Rounds list"]:
                print(elements)
        except ValueError:
            print()
            print("You must enter a valid number.")
            Controller.rounds_in_tournament(self)
        print()

    def tournament_winner(self):
        """Show the winner at the end of the tournament."""
        print()
        print("The winner of the tournament is :")
        print((RANKING[0][0]).strip(), (RANKING[0][1]).strip())
        print()
        print()
        print("The rest of the tournament ranking :")
        for elements in RANKING[1:]:
            print(elements)
        print()
