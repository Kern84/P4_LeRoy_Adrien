PLAYERS_DATABASE = []


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
        return firstname.capitalize(), name.upper(), birthdate, gender, abs(int(elo)), abs(float(rank))

    def add_players(self):
        """Add players to the tournament."""
        number_of_players = abs(int(input("Number of players : ")))
        for i in range(number_of_players):
            print("Player " + str(i+1))
            players = self.prompt_for_player()
            PLAYERS_DATABASE.append(players)

    def match_results(self, victories=0, draws=0, losses=0):
        """Match results."""
        self.victories = victories
        self.draws = draws
        self.losses = losses

    def sorting(self):
        """Sorting players by rank then elo.
        For player_pairing() other rounds"""
        return [self[5], self[4]]

    def player_pairing(self):
        """Pairing the players for the first round and the others."""
        first_round = True
        if round == first_round:
            top_tier_elo = sorted(PLAYERS_DATABASE, key=lambda elo: elo[4], reverse=True)[:4]
            low_tier_elo = sorted(PLAYERS_DATABASE, key=lambda elo: elo[4], reverse=True)[4:]
            match1 = top_tier_elo[0], low_tier_elo[0]
            match2 = top_tier_elo[1], low_tier_elo[1]
            match3 = top_tier_elo[2], low_tier_elo[2]
            match4 = top_tier_elo[3], low_tier_elo[3]
            return match1, match2, match3, match4
        else:
            tier_rank = sorted(PLAYERS_DATABASE, key=Player.sorting, reverse=True)
            match1 = tier_rank[0], tier_rank[1]
            match2 = tier_rank[2], tier_rank[3]
            match3 = tier_rank[4], tier_rank[5]
            match4 = tier_rank[6], tier_rank[7]
            return match1, match2, match3, match4

    def player_rank(self):
        """Determine by victories, draws and losses during a tournament"""
        pass


p = Player("", "", "", "", "0", "0")
# John = Player("Margoulin", "John", "24 Juin 1990", "M", "-1200")

p.add_players()
print()
print(PLAYERS_DATABASE)
print()
p.player_pairing()
