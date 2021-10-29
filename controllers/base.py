#from models.player import PLAYER_DICT
#from models.rounds_matchs import Round, Match
#from models.tournament import Tournament

TOURNAMENT_DATABASE = []

REMARKS = []

PLAYERS_DATABASE = {}

SORT = []

MATCHS =[]

ROUNDS = []

PLAYER_DICT = {}



class TournamentController:
    """Define the tournament controller"""

    def __init__(self):
        pass

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

    def remarks(self):
        remark = input("Tournament remarks : ")
        REMARKS.append(remark)


class playerController:
    """Define the player controller."""

    def __init__(self):
        pass

#    def prompt_for_player(self):
        """Prompt for player's infos."""
 #       firstname = input("Player's firstname : ")
 #       PLAYERS_DATABASE["Firstname"] = firstname.capitalize()
 #       name = input("Player's name : ")
 #       PLAYERS_DATABASE["Name"] = name.upper()
 #       birthdate = input("Player's birthdate (yyyy-mm-dd): ")
 #       PLAYERS_DATABASE["Birthdate"] = birthdate
 #       gender = input("Player's gender (male / female): ")
 #       PLAYERS_DATABASE["Gender"] = gender.capitalize()
 #       elo = input("Player's elo : ")
 #       PLAYERS_DATABASE["ELO"] = abs(int(elo))
 #       rank = input("Player's rank : ")
 #       PLAYERS_DATABASE["Rank"] = abs(int(rank))


    def add_players(self):
        """Add players to the tournament."""
        number_of_players = abs(int(input("Number of players : ")))
        for i in range(number_of_players):
            print("Player " + str(i+1))
            firstname = input("Player's firstname : ")
            PLAYERS_DATABASE["Firstname"] = firstname.capitalize()
            name = input("Player's name : ")
            PLAYERS_DATABASE["Name"] = name.upper()
            birthdate = input("Player's birthdate (yyyy-mm-dd): ")
            PLAYERS_DATABASE["Birthdate"] = birthdate
            gender = input("Player's gender (male / female): ")
            PLAYERS_DATABASE["Gender"] = gender.capitalize()
            elo = input("Player's elo : ")
            PLAYERS_DATABASE["ELO"] = abs(int(elo))
            rank = input("Player's rank : ")
            PLAYERS_DATABASE["Rank"] = abs(int(rank))
            PLAYER_DICT["player " + str(i+1)] = PLAYERS_DATABASE


class MatchRoundController:
    """Define the match and round controller."""

    def __init__(self):
        pass

    def prompt_for_round_name(self):
        name = input("Round's name (one, two, ...) : ")
        round_name = "Round " + name.lower()
        return round_name

    def sorting(self):
        """Sorting players by rank then elo.
        For player_pairing() other rounds"""
        return [self[5], self[4]]

    def player_pairing(self):
        """Pairing the players for the first round and the others."""
        round = "Round one"
        if round == MatchRoundController.prompt_for_round_name(self):
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
            tier_rank = sorted(PLAYERS_DATABASE, key=self.sorting, reverse=True)
            match1 = tier_rank[0], tier_rank[1]
            match2 = tier_rank[2], tier_rank[3]
            match3 = tier_rank[4], tier_rank[5]
            match4 = tier_rank[6], tier_rank[7]
            SORT.append(match1)
            SORT.append(match2)
            SORT.append(match3)
            SORT.append(match4)
            return match1, match2, match3, match4

    def match_results(list):
        """Match results."""
        print(MATCHS[0][0])
        result1 = input("Player result (win, draw, lost): ").lower()
        if result1 == "win":           
            MATCHS[0][0][2] += 1
        if result1 == "draw":
            MATCHS[0][0][2] += 0.5
        if result1 == "lost":
            MATCHS[0][0][2] += 0
        print(MATCHS[0][1])
        result2 = input("Player result (win, draw, lost): ").lower()
        if result2 == "win":
            MATCHS[0][1][2] += 1
        if result2 == "draw":
            MATCHS[0][1][2] += 0.5
        if result2 == "lost":
            MATCHS[0][1][2] += 0
        print(MATCHS[1][0])
        result3 = input("Player result (win, draw, lost): ").lower()
        if result3 == "win":
            MATCHS[1][0][2] += 1
        if result3 == "draw":
            MATCHS[1][0][2] += 0.5
        if result3 == "lost":
            MATCHS[1][0][2] += 0
        print(MATCHS[1][1])
        result4 = input("Player result (win, draw, lost): ").lower()
        if result4 == "win":
            MATCHS[1][1][2] += 1
        if result4 == "draw":
            MATCHS[1][1][2] += 0.5
        if result4 == "lost":
            MATCHS[1][1][2] += 0
        print(MATCHS[2][0])
        result5 = input("Player result (win, draw, lost): ").lower()
        if result5 == "win":
            MATCHS[2][0][2] += 1
        if result5 == "draw":
            MATCHS[2][0][2] += 0.5
        if result5 == "lost":
            MATCHS[2][0][2] += 0
        print(MATCHS[2][1])
        result6 = input("Player result (win, draw, lost): ").lower()
        if result6 == "win":
            MATCHS[2][1][2] += 1
        if result6 == "draw":
            MATCHS[2][1][2] += 0.5
        if result6 == "lost":
            MATCHS[2][1][2] += 0
        print(MATCHS[3][0])
        result7 = input("Player result (win, draw, lost): ").lower()
        if result7 == "win":
            MATCHS[3][0][2] += 1
        if result7 == "draw":
            MATCHS[3][0][2] += 0.5
        if result7 == "lost":
            MATCHS[3][0][2] += 0
        print(MATCHS[3][1])
        result8 = input("Player result (win, draw, lost): ").lower()
        if result8 == "win":
            MATCHS[3][1][2] += 1
        if result8 == "draw":
            MATCHS[3][1][2] += 0.5
        if result8 == "lost":
            MATCHS[3][1][2] += 0
        return result1, result2, result3, result4, result5, result6, result7, result8

    def player_rank(self, victories=1, draws=0.5, losses=0):
        """Determine by victories, draws and losses during a tournament"""
        self.victories = victories
        self.draws = draws
        self.losses = losses


p = playerController()
p.add_players()
print()
print(PLAYERS_DATABASE)
print()
print(PLAYER_DICT)