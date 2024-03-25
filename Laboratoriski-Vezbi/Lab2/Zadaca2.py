from searching_framework import Problem, astar_search

import math


def validate_state(state, obstacles, width):
    person = state
    if person in obstacles:
        return False
    if person[0] < 0 or person[0] >= width or person[1] < 0 or person[1] >= width:
        return False
    return True


def manhattan_distance(state1, state2):
    return (state1[0] - state2[0]) + abs(state1[1] - state2[1])


def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def move_left(state, obstacles, width):
    person = list(state)
    person[0] -= 1
    new_state = tuple(person)
    if validate_state(new_state, obstacles, width):
        return new_state
    else:
        return state


def move_up(state, obstacles, width):
    person = list(state)
    person[1] += 1
    new_state = tuple(person)
    if validate_state(new_state, obstacles, width):
        return new_state
    else:
        return state


def move_down(state, obstacles, width):
    person = list(state)
    person[1] -= 1
    new_state = tuple(person)
    if validate_state(new_state, obstacles, width):
        return new_state
    else:
        return state


def move_right_1(state, obstacles, width):
    person = list(state)
    person[0] += 1
    new_state = tuple(person)
    if validate_state(new_state, obstacles, width):
        return new_state
    else:
        return state


def move_right_2(state, obstacles, width):
    person = list(state)
    person[0] += 2
    new_state = tuple(person)
    if validate_state(new_state, obstacles, width) and move_right_1(state, obstacles,
                                                                    width) != state:  # da ne se preskokvit obstacle
        return new_state
    else:
        return state


def move_right_3(state, obstacles, width):
    person = list(state)
    person[0] += 3
    new_state = tuple(person)
    if validate_state(new_state, obstacles, width) and move_right_2(state, obstacles, width) != state:
        return new_state
    else:
        return state


class Lavirint(Problem):
    # State = (x_person, y_person)
    def __init__(self, initial, obstacles, width, house, goal=None):
        super().__init__(initial, goal)
        self.obstacles = obstacles
        self.house = house
        self.width = width
        self.height = width

    def successor(self, state):
        possible_moves = dict()

        new_state = move_up(state, self.obstacles, self.width)
        if new_state != state:
            possible_moves["Gore"] = new_state

        new_state = move_down(state, self.obstacles, self.width)
        if new_state != state:
            possible_moves["Dolu"] = new_state

        new_state = move_left(state, self.obstacles, self.width)
        if new_state != state:
            possible_moves["Levo"] = new_state

        new_state = move_right_2(state, self.obstacles, self.width)
        if new_state != state:
            possible_moves["Desno 2"] = new_state

        new_state = move_right_3(state, self.obstacles, self.width)
        if new_state != state:
            possible_moves["Desno 3"] = new_state

        return possible_moves

    def actions(self, state):
        return self.successor(state)

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        person = node.state
        house = self.house
        return manhattan_distance(person, house)

    def goal_test(self, state):
        person = state
        return person == self.house


if __name__ == '__main__':
    width = int(input())
    n = int(input())
    obstacles = []
    for i in range(n):
        obstacle = tuple(map(int, input().split(",")))
        obstacles.append(obstacle)
    person = tuple(map(int, input().split(",")))
    person = tuple(person)
    house = tuple(map(int, input().split(",")))
    obstacles = tuple(obstacles)
    problem = Lavirint(person, obstacles, width, house)
    solution = astar_search(problem)

    if solution is not None:
        print(solution.solution())
    else:
        print("[]")
