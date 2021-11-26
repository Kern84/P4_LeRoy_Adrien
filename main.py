from controllers.base import Controller

from views.base import Views


def main():
    """To start the app."""
    view = Views()
    control = Controller()

    view.start_menu()
    control.start_menu_tournament()
    control.tournament_execution()


if __name__ == "__main__":
    main()
