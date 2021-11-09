import sys

from models.player import Player, PLAYERS_DATABASE, PLAYERS_IN_TOURNAMENT
from models.tournament import Tournament, TOURNAMENTS_DATABASE
from models.rounds_matchs import Match, Round

from views.base import Views

TOURNAMENT_REMARKS = []

SORT = []

ROUNDS = []

TOURNAMENT_RANK = []


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
        Views.rounds_menu(self)


class PlayerController:
    """Define the player controller."""

    def __init__(self):
        pass

    def choice_for_add_players_menu(self):
        """Menu to add players to the tournament.
        1 = add players from database; 2 = Create players; 3 = Start the tournament; 4 = exit."""
        menu_choice = abs(int(input("Enter the menu number : ")))
        if menu_choice == 1:
            PlayerController.add_players_tournament(self)
            Views.add_players_menu(self)
            PlayerController.choice_for_add_players_menu(self)
        if menu_choice == 2:
            number_of_players_to_add = abs(int(input("Number of players to add : ")))
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
        for elements in enumerate(PLAYERS_DATABASE):
            print(elements)
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
            print(PLAYERS_IN_TOURNAMENT)
        if len(PLAYERS_IN_TOURNAMENT) > 8:
            print("The tournament must consists of height players. Please remove players.")
            for index in enumerate(PLAYERS_DATABASE):
                print(index)
            player_to_remove = abs(int(input("Enter the player's number to remove from the tournament : ")))
            del PLAYERS_IN_TOURNAMENT[player_to_remove]
            PlayerController.checking_number_of_players(self)
        if len(PLAYERS_IN_TOURNAMENT) < 8:
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

    def paring_players_other_rounds(self):
        print("other rounds pairing")

    def end_of_matches(self):
        end = input("Enter 'OK' to continue when matches are done : ").upper()
        if end == "OK":
            print(Round.round_date_time(self))
            print()
            MatchRoundController.match_results(self)
            print()
        else:
            print("press 'OK' to continue...")
            MatchRoundController.end_of_matches(self)
            print()

    def match_results(self):
        """Match results."""
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
            TOURNAMENT_RANK.append(points)
            print(PLAYERS_IN_TOURNAMENT[x] + tuple(points))
            x += 1
            print()
        Views.presentation_end_of_matches(self)
        MatchRoundController.end_of_round(self)

    def end_of_round(self):
        """Print at the end of matches. Presenting a quick ranking"""
        provisional_rank = []
        list_rank = []
        x = 0
        for elements in PLAYERS_IN_TOURNAMENT:
            list_rank.append(PLAYERS_IN_TOURNAMENT[x] + tuple(TOURNAMENT_RANK[x]))
            x += 1
        for elements in sorted(list_rank, key=lambda y: (y[5], y[4]), reverse=True):
            provisional_rank.append(elements)
        for elements in enumerate(provisional_rank, start=1):
            print(elements)


"""
    def player_pairing(self):
        Pairing the players for the first round and the others.
        tier_rank = sorted(PLAYERS_DATABASE, key=lambda x: (x[5], x[4]), reverse=True)
        match5 = tier_rank[0], tier_rank[1]
        match6 = tier_rank[2], tier_rank[3]
        match7 = tier_rank[4], tier_rank[5]
        match8 = tier_rank[6], tier_rank[7]
        SORT.append(match5)
        SORT.append(match6)
        SORT.append(match7)
        SORT.append(match8)
        return match5, match6, match7, match8
"""
