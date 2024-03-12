"""
Defining a class for the problem structure that we will solve with a search.
The Problem class is an abstract class from which we make inheritance to define the basic
characteristics of every problem we want to solve
"""

from searching_framework import Problem, breadth_first_graph_search


# (opaska, telo, telo, telo, telo, telo, glava) - Snake
#
class Snake_Game(Problem):
    def __init__(self, snake, green_apples, red_apples):
        initial = (snake, green_apples, 'dolu')
        super().__init__(initial)
        self.red_apples = red_apples
        self.width = 10
        self.height = 10

    def successor(self, state):
        possible_moves = dict()
        new_state = self.prodolziNapred(state)
        if self.is_move_valid(state):
            possible_moves["ProdolzhiPravo"] = new_state
        new_state = self.svrtiDesno(state)
        if self.is_move_valid(new_state):
            possible_moves["SvrtiDesno"] = new_state
        new_state = self.SvrtiLevo(state)
        if self.is_move_valid(new_state):
            possible_moves["SvrtiLevo"] = new_state

        return possible_moves

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        green_apples = state[1]
        return len(green_apples) == 0

    def is_move_valid(self, state):
        snake = state[0]
        snake_head = snake[-1]
        if snake_head[0] < 0 or snake_head[0] >= self.width or snake_head[1] < 0 or snake_head[1] >= self.height:
            return False
        # for telo in snake[:-1]:
        #     if telo[0] == snake_head[0] and telo[1] == snake_head[1]:
        #         return False
        if snake_head in snake[:-1]:
            return False
        if snake_head in self.red_apples:
            return False
        return True

    def prodolziNapred(self, state):
        snake = list(state[0])
        snake_head = snake[-1]
        orientacija = state[2]
        if orientacija == 'gore':
            snake.append((snake_head[0], snake_head[1] + 1))
        elif orientacija == 'dolu':
            snake.append((snake_head[0], snake_head[1] - 1))
        elif orientacija == 'levo':
            snake.append((snake_head[0] - 1, snake_head[1]))
        elif orientacija == 'desno':
            snake.append((snake_head[0] + 1, snake_head[1]))

        snake_head = snake[-1]
        green_apples = list(state[1])

        if snake_head in green_apples:
            for apple in green_apples:
                if apple == snake_head:
                    green_apples.remove(apple)
        else:
            snake = snake[1:]

        snake = tuple(snake)
        green_apples = tuple(green_apples)
        return snake, green_apples, orientacija

    def svrtiDesno(self, state):
        snake = list(state[0])
        snake_head = snake[-1]
        orientacija = state[2]
        if orientacija == 'gore':
            snake.append((snake_head[0]+1, snake_head[1]))
            orientacija = 'desno'
        elif orientacija == 'dolu':
            snake.append((snake_head[0]-1, snake_head[1]))
            orientacija = 'levo'
        elif orientacija == 'levo':
            snake.append((snake_head[0], snake_head[1] + 1))
            orientacija = 'gore'
        elif orientacija == 'desno':
            snake.append((snake_head[0], snake_head[1] - 1))
            orientacija = 'dolu'

        snake_head = snake[-1]
        green_apples = list(state[1])

        if snake_head in green_apples:
            for apple in green_apples:
                if apple == snake_head:
                    green_apples.remove(apple)
        else:
            snake = snake[1:]

        snake = tuple(snake)
        green_apples = tuple(green_apples)
        return snake, green_apples, orientacija

    def SvrtiLevo(self, state):
        snake = list(state[0])
        snake_head = snake[-1]
        orientacija = state[2]
        if orientacija == 'gore':
            snake.append((snake_head[0] - 1, snake_head[1]))
            orientacija = 'levo'
        elif orientacija == 'dolu':
            snake.append((snake_head[0] + 1, snake_head[1]))
            orientacija = 'desno'
        elif orientacija == 'levo':
            snake.append((snake_head[0], snake_head[1] - 1))
            orientacija = 'dolu'
        elif orientacija == 'desno':
            snake.append((snake_head[0], snake_head[1] + 1))
            orientacija = 'gore'

        snake_head = snake[-1]
        green_apples = list(state[1])

        if snake_head in green_apples:
            for apple in green_apples:
                if apple == snake_head:
                    green_apples.remove(apple)
        else:
            snake = snake[1:]

        snake = tuple(snake)
        green_apples = tuple(green_apples)
        return snake, green_apples, orientacija


if __name__ == '__main__':
    n = int(input())
    green = []

    for i in range(0, n):
        apple = input().split(',')
        apple = [int(apple[0]), int(apple[1])]
        green.append(tuple(apple))

    m = int(input())
    red = []

    for i in range(0, m):
        apple = input().split(',')
        apple = [int(apple[0]), int(apple[1])]
        red.append(tuple(apple))

    s = ((0, 9), (0, 8), (0, 7))
    orien = 'dolu'

    snake_problem = Snake_Game(s, tuple(green), tuple(red))
    print(breadth_first_graph_search(snake_problem).solution())