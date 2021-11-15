from models.player import Player, PLAYERS_DATABASE
from models.rounds_matchs import Round, Match
from models.tournament import Tournament, TOURNAMENTS_DATABASE

from controllers.base import TournamentController, PlayerController, MatchRoundController, PLAYERS_IN_TOURNAMENT

from views.base import Views


def main():
    view = Views()
    tour_control = TournamentController()

    view.start_menu()
    tour_control.start_menu_tournament()
    tour_control.tournament_execution()


if __name__ == "__main__":
    main()
