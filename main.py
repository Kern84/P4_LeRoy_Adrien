from controllers.base import TournamentController

from views.base import Views


def main():
    view = Views()
    tour_control = TournamentController()

    view.start_menu()
    tour_control.start_menu_tournament()
    tour_control.tournament_execution()


if __name__ == "__main__":
    main()
