from settings import PUZZLE_SIZE, EMPTY_CELL_VALUE
from random import shuffle


def is_correct(puzzle):
    # TODO : vérifier si le jeu est gagné
    pass


def randomize_puzzle():
     while "unsolvable puzzle":
        puzzle = create_list()
        if is_solvable_and_empty_at_end(puzzle):
            return [list(a) for a in zip(*[iter(puzzle)] * PUZZLE_SIZE)]


def create_list():
    puzzle_list = list(range(1, PUZZLE_SIZE ** 2))
    shuffle(puzzle_list)
    puzzle_list.append(EMPTY_CELL_VALUE)
    return puzzle_list


def is_solvable_and_empty_at_end(puzzle_list):
    inversion = 0
    i = 0
    while i < len(puzzle_list) - 2:
        j = i+1
        while j < len(puzzle_list) - 1:
            if puzzle_list[i] > puzzle_list[j]:
                inversion += 1
            j += 1
        i += 1
    return (inversion % 2 == 0) and (puzzle_list[-1] == EMPTY_CELL_VALUE)


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


if __name__ == '__main__':
    puzzle = create_list()
    print(is_solvable_and_empty_at_end(puzzle))