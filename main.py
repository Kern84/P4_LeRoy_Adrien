from models.player import Player, PLAYERS_DATABASE
from models.rounds_matchs import Round, Match
from models.tournament import Tournament, TOURNAMENTS_DATABASE

from controllers.base import TournamentController, PlayerController, MatchRoundController, PLAYERS_IN_TOURNAMENT

from views.base import Views


def main():
    view = Views()
    rounds = Round()
    tour = Tournament()
    tour_control = TournamentController()
    player_control = PlayerController()
    match_round_control = MatchRoundController()

    view.start_menu()
    tour_control.start_menu_tournament()
    print()
    view.add_players_menu()
    player_control.choice_for_add_players_menu()
    print()
    print(rounds.round_date_time())
    view.rounds_menu()
    print()
    match_round_control.round_affector()
    print()
    view.matchs_presentation_menu()
    print()
    match_round_control.end_of_matches()
    print()


if __name__ == "__main__":
    main()
