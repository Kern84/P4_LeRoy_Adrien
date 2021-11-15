import sys

from models.player import Player, PLAYERS_DATABASE, PLAYERS_IN_TOURNAMENT
from models.tournament import Tournament, TOURNAMENTS_DATABASE
from models.rounds_matchs import Match, Round, MATCHS, ROUNDS

from views.base import Views

TOURNAMENT_REMARKS = []

TOURNAMENT_RANK = []

RANKING = []

PROVISIONAL_MATCHES = []

LIST_RANK = []


class TournamentController:
    """Define the tournament controller"""

    def __init__(self):
        pass

    def start_menu_tournament(self):
        """Start menu for the tournament. 1 = create tournament; 2 = consult previous tournaments;
            3 = consult players in database; 4 = exit."""
        menu_choice = abs(int(input("Enter the menu number : ")))
        if menu_choice == 1:
            TournamentController.prompt_for_create_tournament(self)
            print()
            print("Tournament :")
            print(TOURNAMENTS_DATABASE[-1])
            print()
            Views.add_players_menu(self)
            PlayerController.choice_for_add_players_menu(self)
        if menu_choice == 2:
            print()
            print("Tournaments :")
            for elements in enumerate(TOURNAMENTS_DATABASE):
                print(elements)
            Views.start_menu(self)
            TournamentController.start_menu_tournament(self)
        if menu_choice == 3:
            print()
            print("Players :")
            for elements in enumerate(PLAYERS_DATABASE):
                print(elements)
            Views.start_menu(self)
            TournamentController.start_menu_tournament(self)
        if menu_choice == 4:
            sys.exit()

    def prompt_for_create_tournament(self):
        """Prompt for tournament's info."""
        return Tournament(
            name=input("Tournament's name : ").capitalize(),
            place=input("Place of the tournament : ").capitalize(),
            start_date=input("Tournament start date (yyyy-mm-dd) : "),
            end_date=input("Tournament end date (yyyy-mm-dd) : "),
            game_type=input("Tournament type of game (Blitz, Bullet, Quick): ").capitalize(),
            number_of_rounds=abs(int(input("Number of rounds in the tournament : ")))
        )

    def remarks(self):
        remark = input("Tournament remarks : ")
        TOURNAMENT_REMARKS.append(remark)

    def start_tournament(self):
        PlayerController.checking_number_of_players(self)

    def tournament_execution(self):
        for rounds in range(TOURNAMENTS_DATABASE[-1][5]):
            Views.rounds_menu(self)
            MatchRoundController.round_affector(self)
            Views.matchs_presentation_menu(self)
            MatchRoundController.end_of_matches(self)
            MatchRoundController.closing_of_round(self)
        TournamentController.remarks(self)
        Views.end_tournament(self)


class PlayerController:
    """Define the player controller."""

    def __init__(self):
        pass

    def choice_for_add_players_menu(self):
        """Menu to add players to the tournament.
        1 = add players from database; 2 = Create players; 3 = Start the tournament; 4 = exit."""
        menu_choice = abs(int(input("Enter the menu number : ")))
        print()
        if menu_choice == 1:
            PlayerController.add_players_tournament(self)
            Views.add_players_menu(self)
            PlayerController.choice_for_add_players_menu(self)
        if menu_choice == 2:
            number_of_players_to_add = abs(int(input("Number of players to add : ")))
            print()
            for i in range(number_of_players_to_add):
                print("Player " + str(i + 1))
                PlayerController.create_player(self)
            Views.add_players_menu(self)
            PlayerController.choice_for_add_players_menu(self)
        if menu_choice == 3:
            TournamentController.start_tournament(self)
        if menu_choice == 4:
            sys.exit()

    def create_player(self):
        """Create players for database and tournament. Prompt for players info."""
        return Player(
            firstname=input("Player's firstname : ").capitalize(),
            name=input("Player's name : ").upper(),
            birthdate=input("Player's birthdate (yyyy-mm-dd): "),
            gender=input("Player's gender (male / female): ").capitalize(),
            elo=abs(int(input("Player's elo : ")))
        )

    def add_players_tournament(self):
        """Add players who are already in the PLAYERS_DATABASE."""
        players_to_add = abs(int(input("Number of database players to add to the tournament : ")))
        print()
        for elements in enumerate(PLAYERS_DATABASE):
            print(elements)
        print()
        x = 0
        while x in range(players_to_add):
            player_num = abs(int(input("Enter the player's number to add to the tournament : ")))
            player = PLAYERS_DATABASE[player_num]
            PLAYERS_IN_TOURNAMENT.append(player)
            print("Player added to the tournament.")
            print()
            x += 1
        print()

    def checking_number_of_players(self):
        """Checking if the number of players in tge tournament equal 8."""
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
            for index in enumerate(PLAYERS_DATABASE):
                print(index)
            player_to_remove = abs(int(input("Enter the player's number to remove from the tournament : ")))
            del PLAYERS_IN_TOURNAMENT[player_to_remove]
            PlayerController.checking_number_of_players(self)
        if len(PLAYERS_IN_TOURNAMENT) < 8:
            print()
            print("Not enough players in the tournament. Please add some.")
            Views.add_players_menu(self)
            PlayerController.choice_for_add_players_menu(self)


class MatchRoundController:
    """Define the match and round controller."""

    def __init__(self):
        pass

    def prompt_for_round_name(self):
        """Prompt for registering the number of the round."""
        name = input("Round (one, two, ...) : ")
        round_name = "Round " + name.lower()
        print()
        print(round_name)
        print(Round.round_date_time(self))
        print()
        return round_name

    def round_affector(self):
        """variable for choosing the round."""
        if MatchRoundController.prompt_for_round_name(self) == "Round one":
            MatchRoundController.pairing_players_round_one(self)
        else:
            MatchRoundController.pairing_players_other_rounds(self)

    def pairing_players_round_one(self):
        """Pairing players for the first round."""
        top_tier_elo = sorted(PLAYERS_IN_TOURNAMENT, key=lambda elo: elo[4], reverse=True)[:4]
        low_tier_elo = sorted(PLAYERS_IN_TOURNAMENT, key=lambda elo: elo[4], reverse=True)[4:]
        match1 = top_tier_elo[0], low_tier_elo[0],
        match2 = top_tier_elo[1], low_tier_elo[1],
        match3 = top_tier_elo[2], low_tier_elo[2],
        match4 = top_tier_elo[3], low_tier_elo[3]
        return Match(match1, match2, match3, match4)

    def pairing_players_other_rounds(self):
        """Pairing players for all rounds except the first round."""
        PROVISIONAL_MATCHES.clear()
        tier_rank = sorted(RANKING, key=lambda y: (y[5], y[4]), reverse=True)
        x = 0
        z = 1
        for i in range(4):
            match = tier_rank[x], tier_rank[z]
            if match not in MATCHS:
                PROVISIONAL_MATCHES.append(match)
                x += 2
                z += 2
            else:
                print("The match {} against {} as already been played.".format(tier_rank[x], tier_rank[z]))
                for n in range(8):
                    z += 1
                    match = tier_rank[x], tier_rank[z]
                    if match not in ROUNDS:
                        PROVISIONAL_MATCHES.append(match)
                        x += 1
                        z += 1
                        break
                    else:
                        print("The match {} against {} as already been played.".format(tier_rank[x], tier_rank[z]))
                        z += 1
        MatchRoundController.other_rounds_matches(self)

    def other_rounds_matches(self):
        match1 = PROVISIONAL_MATCHES[0]
        match2 = PROVISIONAL_MATCHES[1]
        match3 = PROVISIONAL_MATCHES[2]
        match4 = PROVISIONAL_MATCHES[3]
        return Match(match1, match2, match3, match4)

    def end_of_matches(self):
        print()
        end = input("Enter 'OK' to continue when matches are done : ").upper()
        if end == "OK":
            print()
            if len(MATCHS) <= 4:
                MatchRoundController.match_results_round_one(self)
            else:
                MatchRoundController.match_results_others(self)
            print()
        else:
            print("press 'OK' to continue...")
            MatchRoundController.end_of_matches(self)
            print()

    def match_results_round_one(self):
        """Match results round one."""
        x = 0
        for player in PLAYERS_IN_TOURNAMENT:
            points = [0]
            print(PLAYERS_IN_TOURNAMENT[x])
            result = input("Player result (win, draw, lost): ").lower()
            if result == "win":
                points[0] += 1
            if result == "draw":
                points[0] += 0.5
            if result == "lost":
                points[0] += 0
            else:
                MatchRoundController.match_results_round_one(self)
            TOURNAMENT_RANK.append(points)
            print(PLAYERS_IN_TOURNAMENT[x] + tuple(points))
            x += 1
            print()
        Views.presentation_end_of_matches(self)
        MatchRoundController.end_of_round_one(self)

    def match_results_others(self):
        """Match results other rounds."""
        x = 0
        for player in RANKING:
            print(RANKING[x])
            result = input("Player result (win, draw, lost): ").lower()
            l = list(RANKING)
            if result == "win":
                l[x][5] += 1
            if result == "draw":
                l[x][5] += 0.5
            if result == "lost":
                l[x][5] += 0
            print(l[x])
            x += 1
            print()
        Views.presentation_end_of_matches(self)
        MatchRoundController.end_of_other_rounds(self)

    def end_of_round_one(self):
        """Print at the end of matches. Presenting a quick ranking"""
        x = 0
        for elements in PLAYERS_IN_TOURNAMENT:
            LIST_RANK.append(PLAYERS_IN_TOURNAMENT[x] + tuple(TOURNAMENT_RANK[x]))
            x += 1
        for elements in sorted(LIST_RANK, key=lambda y: (y[5], y[4]), reverse=True):
            RANKING.append(elements)
        for elements in enumerate(RANKING, start=1):
            print(elements)

    def end_of_other_rounds(self):
        for elements in enumerate(sorted(RANKING, key=lambda y: (y[5], y[4]), reverse=True), start=1):
            print(elements)

    def closing_of_round(self):
        choice = input("Closing of this round and start of a new one ? (yes / no) : ").lower()
        if choice == "yes":
            print()
            print(Round.round_date_time(self))
            print()
        else:
            print()
            MatchRoundController.closing_of_round(self)
