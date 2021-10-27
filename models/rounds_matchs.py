from datetime import datetime



MATCHS = [((('C', 'C', '3', 'F', 3000, 1.0), ('G', 'G', '7', 'M', 1100, 0.0)),
            (('H', 'H', '8', 'F', 2300, 0.0), ('A', 'A', '1', 'M', 1000, 1.0)),
            (('E', 'E', '5', 'F', 2100, 0.5), ('F', 'F', '6', 'F', 800, 0.5)),
            (('B', 'B', '2', 'F', 2000, 1.0), ('D', 'D', '4', 'M', 400, 0.5)))]
ROUNDS = []


class Round:
    """Class Round.
    A round consists of four matches."""

    def __init__(self, name):
        self.name = name

    def prompt_for_round_name(self):
        name = input("Round's name (one, two, ...) : ")
        round_name = "Round " + name.lower()
        return round_name

    def round_date_time(self):
        """Automatically saves starting / ending date and time"""
        now = datetime.now()
        time_now = now.strftime("%Y-%m-%d, %H:%M:%S")
        return time_now

    def matchs_per_round(self):
        round1 = MATCHS[:4]
        round2 = MATCHS[4:8]
        round3 = MATCHS[8:12]
        round4 = MATCHS[12:]
        matchs_round = round1, round2, round3, round4
        ROUNDS.append(matchs_round)

    def new_round(self):
        pass


class Match:
    """Class Match."""

    def __init__(self, name):
        self.name = name

    def match_list(self):
        matchs = None
        MATCHS.append(matchs)
        print(MATCHS)


round = Round("")
m = Match("")
round.matchs_per_round()
print(ROUNDS)
#m.match_list()
#round.prompt_for_round_name()
#print(round.prompt_for_round_name())


