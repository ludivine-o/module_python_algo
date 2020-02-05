from models import move, is_correct, randomize_puzzle, ordered_puzzle, get_empty_cell_location
from settings import PUZZLE_SIZE


def get_available_movement(puzzle):
    movement = ["LEFT", "RIGHT", "UP", "DOWN"]
    x_axis, y_axis = get_empty_cell_location(puzzle)
    if x_axis == 0:
        movement.remove("UP")
    if x_axis == PUZZLE_SIZE-1:
        movement.remove("DOWN")
    if y_axis == 0:
        movement.remove("LEFT")
    if y_axis == PUZZLE_SIZE-1:
        movement.remove("RIGHT")
    return movement


def make_move(direction, puzzle):
    available_movement = get_available_movement(puzzle)
    if direction in available_movement:
        puzzle = move(direction, puzzle)
    return puzzle


def has_won(puzzle):
    is_correct(puzzle)


def get_random_puzzle():
    puzzle = randomize_puzzle()
    return puzzle


def get_ordered_puzzle():
    return ordered_puzzle()