from controllers.base import Controller
from models.tournament import CURRENT_TOURNAMENT

from views.base import Views


def main():
    """To start the app."""
    view = Views()
    control = Controller()

    view.start_menu()
    view.start_menu_tournament()
    for rounds in range(CURRENT_TOURNAMENT[0][5]):
        view.rounds_menu()
        control.round_affector()
        view.matchs_presentation_menu()
        view.end_of_matches()
        view.closing_of_round()
    view.prompt_for_save_tournament()
    view.tournament_winner()
    view.end_tournament()
    view.end_of_tournament()


if __name__ == "__main__":
    main()
