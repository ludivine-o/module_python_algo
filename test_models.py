from models import move
from settings import PUZZLE_SIZE, EMPTY_CELL_VALUE

cases = list(range(1, PUZZLE_SIZE ** 2)) + [EMPTY_CELL_VALUE]
puzzle = [list(a) for a in zip(*[iter(cases)] * PUZZLE_SIZE)]
print(puzzle)

puzzleleft = puzzle
puzzleleft[3][3] = puzzle[3][2]
puzzleleft[3][2] = EMPTY_CELL_VALUE
print(puzzleleft)

def test_move():
    result_puzzle = move("DOWN", puzzle)
    print(result_puzzle)
    assert result_puzzle == puzzleleft

test_move()