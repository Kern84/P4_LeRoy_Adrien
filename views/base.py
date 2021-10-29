from controllers.base import Controller, SORT, MATCHS

class Views:
    """Class Views.
    Implement the views."""

    def __init__(self):
        pass

    def match_display(self):
        first_player = (SORT[0][0][0], SORT[0][0][1], SORT[0][0][5])
        second_player = (SORT[0][1][0], SORT[0][1][1], SORT[0][1][5])
        third_player = (SORT[1][0][0], SORT[1][0][1], SORT[1][0][5])
        fourth_player = (SORT[1][1][0], SORT[1][1][1], SORT[1][1][5])
        fifth_player =(SORT[2][0][0], SORT[2][0][1], SORT[2][0][5])
        sixth_player = (SORT[2][1][0], SORT[2][1][1], SORT[2][1][5])
        seventh_player =(SORT[3][0][0], SORT[3][0][1], SORT[3][0][5])
        eighth_player = (SORT[3][1][0], SORT[3][1][1], SORT[3][1][5])
        first_match = (first_player, second_player)
        second_match = (third_player, fourth_player)
        third_match = (fifth_player, sixth_player)
        fourth_match = (seventh_player, eighth_player)
        MATCHS.append(first_match)
        MATCHS.append(second_match)
        MATCHS.append(third_match)
        MATCHS.append(fourth_match)
        return first_player, second_player, third_player, fourth_player, fifth_player, sixth_player, seventh_player, eighth_player
