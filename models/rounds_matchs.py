MATCHS = []

ROUNDS = []


class Round:
    """Class Round.
    A round consists of four matches."""

    def __init__(self, name, start_time, end_time, match_list):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.match_list = match_list
        ROUNDS.append(self.round)


class Match:
    """Class Match."""

    def __init__(self, player_one, score_one, player_two, score_two):
        self.player_one = player_one
        self.score_one = score_one
        self.player_two = player_two
        self.score_two = score_two
        p1 = self.player_one, self.score_one
        p2 = self.player_two, self.score_two
        match = p1, p2
        MATCHS.append(match)

    def from_matches_to_rounds(self):
        pass
