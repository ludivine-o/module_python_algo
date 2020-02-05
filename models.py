from settings import PUZZLE_SIZE, EMPTY_CELL_VALUE
from random import shuffle


def is_correct(puzzle):
    # TODO : vérifier si le jeu est gagné
    pass


def randomize_puzzle():
    # TODO : certains états random ne sont pas solvables,
    # il faut que cette fonction ne renvoie que des états solvables
    # TODO : changer en def randomize_puzzle(puzzle)
    cases = list(range(1, PUZZLE_SIZE ** 2)) + [EMPTY_CELL_VALUE]
    shuffle(cases)
    return [list(a) for a in zip(*[iter(cases)] * PUZZLE_SIZE)]


def move(direction, puzzle):
    x_axis_empty_cell, y_axis_empty_cell = get_empty_cell_location(puzzle)
    x_axis_target_cell = x_axis_empty_cell
    y_axis_target_cell = y_axis_empty_cell
    if direction == "UP":
        x_axis_empty_cell -= 1
    if direction == "DOWN":
        x_axis_empty_cell += 1
    if direction == "LEFT":
        y_axis_empty_cell -= 1
    if direction == "RIGHT":
        y_axis_empty_cell += 1
    puzzle[x_axis_target_cell][y_axis_target_cell] = puzzle[x_axis_empty_cell][y_axis_empty_cell]
    puzzle[x_axis_empty_cell][y_axis_empty_cell] = EMPTY_CELL_VALUE
    return puzzle


def ordered_puzzle():
    cases = list(range(1, PUZZLE_SIZE ** 2)) + [EMPTY_CELL_VALUE]
    return [list(a) for a in zip(*[iter(cases)] * PUZZLE_SIZE)]


def get_empty_cell_location(puzzle):
    for x, list in enumerate(puzzle):
        for y, cell in enumerate(list):
            if cell == EMPTY_CELL_VALUE:
                return x, y