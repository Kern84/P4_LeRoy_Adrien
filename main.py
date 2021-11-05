from models.player import Player, PLAYERS_DATABASE
from models import rounds_matchs
from models import tournament

from controllers.base import TournamentController, PlayerController, MatchRoundController, SORT

from views.base import Views


def main():
    view = Views()
    tour_control = TournamentController()
    player_control = PlayerController()
    match_round_control = MatchRoundController()

    view.start_menu()
    tour_control.start_menu_tournament()
    print()
    print(tournament.Tournament)
    view.add_players_menu()
    player_control.choice_for_add_players_menu()
    print()
    print(PLAYERS_DATABASE)
    print()
    view.rounds_menu()
    match_round_control.round_affector()
    print()
    print(view.matchs_presentation_menu())


if __name__ == "__main__":
    main()
