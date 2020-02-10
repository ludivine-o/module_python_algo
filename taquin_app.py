from console_ui import clear_ui, init_ui, display_output, handle_keypress
from taquin_controler import get_random_solvable_puzzle, get_ordered_puzzle

import curses


def main():
    """Fonction principale de l'application"""
    try:
        # Initalisation de l'UI
        ui = init_ui()

        # Récupération d'un taquin tiré aléatoirement
        puzzle = get_random_solvable_puzzle()

        while True:
            # Attend une action et affiche le résultat
            puzzle = handle_keypress(puzzle)
            display_output(puzzle)

            # Frequence de rafraichissement
            curses.napms(50)  # ms
    except KeyboardInterrupt:
        pass
    finally:
        # Lorsqu'on quite, on restaure l'environnement du terminal
        clear_ui()


if __name__ == "__main__":
    main()
