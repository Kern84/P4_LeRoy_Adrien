from models.player import Player
from models.rounds_matchs import Round, Match
from models.tournament import Tournament

from controllers.base import Controller, PLAYERS_DATABASE, SORT, MATCHS, ROUNDS

from views.base import Views


def main():
    player = Player()
    round = Round()
    match = Match()
    tournament = Tournament()
    controller = Controller()
    views = Views()

if __name__ == "__main__":
    main()