import random
import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"

random.seed(0)


class Player:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, position):
        self.x_pos, self.y_pos = position
        print(f"[{position[0]}, {position[1]}]")


class Game:
    def __init__(self, width, height, matrix):
        self.width = width
        self.height = height
        self.matrix = matrix

    def has_points_left(self):
        for row in self.matrix:
            if '.' in row:
                return True
        return False

    def possible_moves(self, player):
        moves = []
        x, y = player.x_pos, player.y_pos
        if x > 0 and self.matrix[x - 1][y] == '.':
            moves.append((x - 1, y))
        if x < self.width - 1 and self.matrix[x + 1][y] == '.':
            moves.append((x + 1, y))
        if y > 0 and self.matrix[x][y - 1] == '.':
            moves.append((x, y - 1))
        if y < self.height - 1 and self.matrix[x][y + 1] == '.':
            moves.append((x, y + 1))
        return moves


class Pacman:
    def __init__(self, width, height, matrix):
        self.player = Player(0, 0)
        self.game = Game(width, height, matrix)

    def eat_item(self, position):
        row_index = position[0]
        column_index = position[1]
        new_value = "#"
        new_array = [row[:] for row in self.game.matrix]
        new_array[row_index][column_index] = new_value
        return new_array

    def play_game(self):
        while self.game.has_points_left():
            moves = self.game.possible_moves(self.player)
            if moves:
                next_move = random.choice(moves)
            else:
                next_move = (random.randint(0, self.game.width - 1), random.randint(0, self.game.height - 1))
            self.game.matrix = self.eat_item(next_move)
            self.player.move(next_move)


if __name__ == "__main__":
    width = int(input())
    height = int(input())
    matrix = []
    for _ in range(height):
        row = list(input().strip())
        matrix.append(row)
    pacman = Pacman(width, height, matrix)
    pacman.play_game()
