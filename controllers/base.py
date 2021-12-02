from models.tournament import PLAYERS_IN_TOURNAMENT
from models.rounds_matchs import Match, MATCHS

from views.base import Views, ROUND_INFOS, RANKING


class Controller:
    """Class Controller.
    Define the tournament controller"""

    def round_affector(self):
        """variable for choosing the round."""
        Views.save_round_name_and_start_time(self)
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
