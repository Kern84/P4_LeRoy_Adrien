from rounds_matchs import Round

PLAYERS_DATABASE = []
MATCHS = []


class Player:
    """Class Player.
    Has a name, a firstname, a birthdate, a gender, an elo and a rank.
    """

    def __init__(self, name, firstname, birthdate, gender, elo, rank):
        self.name = name
        self.firstname = firstname
        self.birthdate = birthdate
        self.gender = gender
        self.elo = elo
        self.rank = rank

    def __str__(self):
        """Used in print."""
        return f"{self.name} {self.firstname}, ELO {self.elo}, Rank {self.rank}"

    def __repr__(self):
        """Used in print."""
        return str(self)

    def prompt_for_player(self):
        """Prompt for player's infos."""
        firstname = input("Player's firstname : ")
        name = input("Player's name : ")
        birthdate = input("Player's birthdate (yyyy-mm-dd): ")
        gender = input("Player's gender (male / female): ")
        elo = input("Player's elo : ")
        rank = input("Player's rank : ")
        return firstname.capitalize(), name.upper(), birthdate, gender.capitalize(), abs(int(elo)), abs(float(rank))

    def add_players(self):
        """Add players to the tournament."""
        number_of_players = abs(int(input("Number of players : ")))
        for i in range(number_of_players):
            print("Player " + str(i+1))
            players = self.prompt_for_player()
            PLAYERS_DATABASE.append(players)

    def sorting(self):
        """Sorting players by rank then elo.
        For player_pairing() other rounds"""
        return [self[5], self[4]]

    def player_pairing(self):
        """Pairing the players for the first round and the others."""
        round = "Round one"
        if round == Round.prompt_for_round_name(self):
            top_tier_elo = sorted(PLAYERS_DATABASE, key=lambda elo: elo[4], reverse=True)[:4]
            low_tier_elo = sorted(PLAYERS_DATABASE, key=lambda elo: elo[4], reverse=True)[4:]
            match1 = top_tier_elo[0], low_tier_elo[0]
            match2 = top_tier_elo[1], low_tier_elo[1]
            match3 = top_tier_elo[2], low_tier_elo[2]
            match4 = top_tier_elo[3], low_tier_elo[3]
            matchs = match1, match2, match3, match4
            MATCHS.append(matchs)
            print(match1)
            print(match2)
            print(match3)
            print(match4)
            return match1, match2, match3, match4
        else:
            tier_rank = sorted(PLAYERS_DATABASE, key=self.sorting, reverse=True)
            match1 = tier_rank[0], tier_rank[1]
            match2 = tier_rank[2], tier_rank[3]
            match3 = tier_rank[4], tier_rank[5]
            match4 = tier_rank[6], tier_rank[7]
            matchs = match1, match2, match3, match4
            MATCHS.append(matchs)
            print(match1)
            print(match2)
            print(match3)
            print(match4)
            return match1, match2, match3, match4

    def match_results(self, victories=0, draws=0, losses=0):
        """Match results."""
        """liste[index] = new """
        self.victories = victories
        self.draws = draws
        self.losses = losses

    def player_rank(self, victories=1, draws=0.5, losses=0):
        """Determine by victories, draws and losses during a tournament"""
        self.victories = victories
        self.draws = draws
        self.losses = losses









p = Player("", "", "", "", "0", "0")
r = Round("")
# John = Player("Margoulin", "John", "24 Juin 1990", "M", "-1200")

p.add_players()
print()
print(PLAYERS_DATABASE)
print()
p.player_pairing()
print()
print(MATCHS)
