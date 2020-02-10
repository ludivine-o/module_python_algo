from taquin_controler import get_random_solvable_puzzle, make_move
from taquin_models import is_solvable_and_empty_at_end


def test_move_up():
    puzzle = [[5, 13, 3, 9], [14, 15, 4, 12], [10, 11, 7, ''], [1, 2, 6, 8]]
    puzzle = make_move("UP", puzzle)
    assert puzzle == [[5, 13, 3, 9], [14, 15, 4, ''], [10, 11, 7, 12], [1, 2, 6, 8]]




def test_is_solvable():

    assert is_solvable_and_empty_at_end(puzzle)


