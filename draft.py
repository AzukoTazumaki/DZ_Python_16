import numpy as np
from random import randint
from collections import namedtuple


class Knight:
    def __init__(self):
        self.size = 6
        x0, y0 = randint(0, self.size - 1), randint(0, self.size - 1)
        self.board = np.zeros((self.size, self.size), dtype=int)
        Move = namedtuple('Move', ['x', 'y'])
        self.moves = Move(1, 2), Move(2, 1), Move(-1, -2), Move(-2, -1), Move(-1, 2), Move(1, -2), Move(-2, 1), Move(2, -1)

    def knights_move(self, x, y, step=1):
        self.board[y, x] = step
        if step < self.size ** 2:
            for move in self.moves:
                dx = move.x + x
                dy = move.y + y
                if (self.size > dx >= 0) and (self.size > dy >= 0) and self.board[dy, dx] == 0:
                    if self.knights_move(dx, dy, step + 1):
                        return True
            self.board[y, x] = 0
            return False
        return True


knight = Knight()
knight.knights_move(1, 5)
print(knight.board)
