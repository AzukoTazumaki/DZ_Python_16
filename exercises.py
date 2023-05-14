import numpy as np
from random import randint
from collections import namedtuple


def common_divisor(two_numbers: str) -> str:
    try:
        first_number = int(two_numbers.split(' ')[0])
        second_number = int(two_numbers.split(' ')[1])
        if first_number == 0:
            return str(second_number)
        return common_divisor(f"{' '.join([str(second_number % first_number), str(first_number)])}")
    except ValueError:
        return 'Ошибка. Введите два числа через пробел.'


class Knight:
    def __init__(self):
        self.size = 6
        x0, y0 = randint(0, self.size - 1), randint(0, self.size - 1)
        self.board = np.zeros((self.size, self.size), dtype=int)
        Move = namedtuple('Move', ['x', 'y'])
        self.moves = Move(1, 2), Move(2, 1), Move(-1, -2), Move(-2, -1), Move(-1, 2), Move(1, -2), Move(-2, 1), Move(2, -1)

    def knights_move(self, coords: str, step=1):
        try:
            coords_list = [int(x) for x in coords.split(' ')]
            x, y = coords_list[0], coords_list[1]
            self.board[y, x] = step
            if step < self.size ** 2:
                for move in self.moves:
                    dx = move.x + x
                    dy = move.y + y
                    if (self.size > dx >= 0) and (self.size > dy >= 0) and self.board[dy, dx] == 0:
                        new_coords_list = ' '.join([str(dx), str(dy)])
                        if self.knights_move(new_coords_list, step + 1):
                            return True
                self.board[y, x] = 0
                return False
            return True
        except ValueError:
            return 'Ошибка.'
