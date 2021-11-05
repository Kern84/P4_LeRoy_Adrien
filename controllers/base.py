from models.player import Player, PLAYERS_DATABASE
from models.tournament import Tournament, Tournaments
from models.rounds_matchs import Match

# from models.rounds_matchs import PLAYERS_DATABASE

TOURNAMENT_DATABASE = []

TOURNAMENT_REMARKS = []

SORT = []

MATCHS = []

ROUNDS = []

PLAYERS_IN_TOURNAMENT = [('PIERCE', 'Paul', 1000, 1),
                         ('ABDUL', 'Paula', 2000, 1),
                         ('LAGIRAFE', 'Sophie', 1200, 1),
                         ('DEFRUIT', 'Juju', 800, 0.5),
                         ('BRYANT', 'Kobe', 3000, 0.5),
                         ('JAMES', 'Lebron', 2300, 0.5),
                         ('JORDAN', 'Mickael', 2800, 0),
                         ('LAREINE', 'Diane', 1500, 0)]


class TournamentController:
    """Define the tournament controller"""

    def __init__(self):
        pass

    def start_menu_tournament(self):
        menu_choice = abs(int(input("Enter the menu number : ")))
        if menu_choice == 1:
            TournamentController.prompt_for_create_tournament(self)
        if menu_choice == 2:
            print("tournaments list")
        if menu_choice == 3:
            print("players database")
        if menu_choice == 4:
            pass

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

    def add_tournament(self):
        """Create a new tournament and add it to the TOURNAMENT_DATABASE."""
        tournament = self.prompt_for_tournament()
        TOURNAMENT_DATABASE.append(tournament)

    def remarks(self):
        remark = input("Tournament remarks : ")
        TOURNAMENT_REMARKS.append(remark)


class PlayerController:
    """Define the player controller."""

    def __init__(self):
        pass

    def choice_for_add_players_menu(self):
        menu_choice = abs(int(input("Enter the menu number : ")))
        if menu_choice == 1:
            print("players database")
        if menu_choice == 2:
            number_of_players_to_add = abs(int(input("Number of players to add : ")))
            for i in range(number_of_players_to_add):
                print("Player " + str(i + 1))
                PlayerController.create_player(self)
        if menu_choice == 3:
            pass

    def prompt_for_players_in_tournament(self):
        number_of_players = abs(int(input("Number of players in the tournament : ")))
        if number_of_players == 8:
            print("Full tournament")
        else:
            print("The tournament must consists of height players.")

    def create_player(self):
        """Create players. Prompt for players info."""
        return Player(
            firstname=input("Player's firstname : ").capitalize(),
            name=input("Player's name : ").upper(),
            birthdate=input("Player's birthdate (yyyy-mm-dd): "),
            gender=input("Player's gender (male / female): ").capitalize(),
            elo=abs(int(input("Player's elo : ")))
        )

    def add_players_tournament(self):
        """Add players who are already in the PLAYERS_DATABASE."""
        for index in enumerate(PLAYERS_DATABASE):
            print(index)
        print(index[0])
        x = 0
        while x in range(8):
            playerx = abs(int(input("Enter the player's number to add to the tournament : ")))
            if playerx == index[0]:
                print("reussi")
            x += 1

    def add_players(self):
        """Add players to the tournament.
        Prompt for player's infos."""
        number_of_players = abs(int(input("Number of players in the tournament : ")))
        if number_of_players == 8:
            for i in range(number_of_players):
                print("Player " + str(i + 1))
                firstname = input("Player's firstname : ")
                name = input("Player's name : ")
                birthdate = input("Player's birthdate (yyyy-mm-dd): ")
                gender = input("Player's gender (male / female): ")
                elo = input("Player's elo : ")
                rank = input("Player's rank : ")
                player = firstname.capitalize(), name.upper(), birthdate, gender.capitalize(), abs(int(elo)), abs(
                    float(rank))
                PLAYERS_DATABASE.append(player)
                return PLAYERS_DATABASE
        else:
            print("The tournament must consists of height players.")


class MatchRoundController:
    """Define the match and round controller."""

    def __init__(self):
        pass

    def prompt_for_round_name(self):
        name = input("Round's name (one, two, ...) : ")
        round_name = "Round " + name.lower()
        return round_name

    def round_affector(self):
        if MatchRoundController.prompt_for_round_name(self) == "Round one":
            MatchRoundController.pairing_players_round_one(self)
        else:
            MatchRoundController.pairing_players_other_rounds(self)

    def pairing_players_round_one(self):
        """Pairing players for the first round."""
        top_tier_elo = sorted(PLAYERS_DATABASE, key=lambda elo: elo[4], reverse=True)[:4]
        low_tier_elo = sorted(PLAYERS_DATABASE, key=lambda elo: elo[4], reverse=True)[4:]
        return Match(
            match1=top_tier_elo[0], low_tier_elo[0],
            match2=top_tier_elo[1], low_tier_elo[1],
            match3=top_tier_elo[2], low_tier_elo[2],
            match4=top_tier_elo[3], low_tier_elo[3]
        )

    def paring_players_other_rounds(self):
        print("other rounds pairing")

    def player_pairing(self):
        """Pairing the players for the first round and the others."""
        round_one = "Round one"
        if round_one == MatchRoundController.prompt_for_round_name(self):
            top_tier_elo = sorted(PLAYERS_DATABASE, key=lambda elo: elo[4], reverse=True)[:4]
            low_tier_elo = sorted(PLAYERS_DATABASE, key=lambda elo: elo[4], reverse=True)[4:]
            match1 = top_tier_elo[0], low_tier_elo[0]
            match2 = top_tier_elo[1], low_tier_elo[1]
            match3 = top_tier_elo[2], low_tier_elo[2]
            match4 = top_tier_elo[3], low_tier_elo[3]
            SORT.append(match1)
            SORT.append(match2)
            SORT.append(match3)
            SORT.append(match4)
            return match1, match2, match3, match4
        else:
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

    def match_results(self):
        """Match results."""
        x = 0
        for player in SORT:
            print(SORT[x][0])
            result = input("Player result (win, draw, lost): ").lower()
            result1 = list(SORT[x][0])
            if result == "win":
                result1[5] += 1
            if result == "draw":
                result1[5] += 0.5
            if result == "lost":
                result1[5] += 0
            print(result1)
            print()
            print(SORT[x][1])
            result = input("Player result (win, draw, lost): ").lower()
            result2 = list(SORT[x][1])
            if result == "win":
                result2[5] += 1
            if result == "draw":
                result2[5] += 0.5
            if result == "lost":
                result2[5] += 0
            match = result1, result2
            print(result2)
            MATCHS.append(match)
            x += 1

    def matchs_per_round(self):
        round1 = MATCHS[:4]
        round2 = MATCHS[4:8]
        round3 = MATCHS[8:12]
        round4 = MATCHS[12:]
        matchs_round = round1, round2, round3, round4
        ROUNDS.append(matchs_round)
