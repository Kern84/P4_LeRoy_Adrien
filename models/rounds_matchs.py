from models.tournament import ROUNDS

MATCHS = []


class Round:
    """Class Round.
    A round consists of four matches, has a name and start/end time."""

    def __init__(self, name, start_time, end_time):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        round = self.name, self.start_time, self.end_time, Round.matches_in_round_list(self)
        ROUNDS.append(round)

    def matches_in_round_list(self):
        matches_list = []
        return matches_list


class Match:
    """Class Match.
    Consist of two players with a score."""

    def __init__(self, player_one, score_one, player_two, score_two):
        self.player_one = player_one
        self.score_one = score_one
        self.player_two = player_two
        self.score_two = score_two
        p1 = self.player_one, self.score_one
        p2 = self.player_two, self.score_two
        match = p1, p2
        Round.matches_in_round_list(self).append(match)
        MATCHS.append(match)
