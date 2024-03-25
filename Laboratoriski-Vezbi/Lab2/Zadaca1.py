from searching_framework import Problem, astar_search


# State (person, house)
# person(x_person, y_person)
# house (x_house, y_house, x_direction)
def manhattan_distance(state1, state2):
    return ((state1[0] - state2[0]) + (state1[1] - state2[1])) / 2


def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def validate_state(state, green_fields):
    person = state[0]
    house = state[1]
    house = tuple(house[:2])
    # if house[0] < 0 or house[0] >= 5 or house[1] < 0 or house[1] >= 9:
    #     return False

    if person[0] < 0 or person[0] >= 5 or person[1] < 0 or person[1] >= 9:
        return False

    if person == house:
        return True

    if person not in green_fields:
        return False

    return True


# house (x_pos, y_pos, direction)
def move_house(state):
    house = list(state[1])
    if house[0] <= 0 or house[0] >= 4:
        house[2] *= -1
        # ne znam zoso e ova vaka
    house[0] += house[2]
    house = tuple(house)
    return house


def move(state, direction, green_fields):
    person = list(state[0])
    house = move_house(state)
    person[0] += direction[0]
    person[1] += direction[1]
    person = tuple(person)
    new_state = (person, house)

    if validate_state(new_state, green_fields):
        return new_state
    else:
        return state


def move_stoj(state, green_fields):
    person = list(state[0])
    house = move_house(state)
    person = tuple(person)
    house = tuple(house)
    new_state = (person, house)
    if validate_state(new_state, green_fields):
        return new_state
    else:
        return state


class Kacuvac(Problem):
    def __init__(self, initial, green_fields, goal=None):
        super().__init__(initial, goal)
        self.green_fields = green_fields

    def successor(self, state):
        possible_moves = dict()

        new_state = move_stoj(state, self.green_fields)
        if new_state != state:
            possible_moves["Stoj"] = new_state

        directions = [(0, 1), (0, 2), (1, 1), (2, 2), (-1, 1), (-2, 2)]
        actions = ["Gore 1", "Gore 2", "Gore-desno 1", "Gore-desno 2", "Gore-levo 1", "Gore-levo 2"]
        for direction, action in zip(directions, actions):
            new_state = move(state, direction, self.green_fields)
            if new_state != state:
                possible_moves[action] = new_state
        # print(possible_moves)
        return possible_moves

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        person = node.state[0]
        house = node.state[1]
        return (person[1] - house[1]) / 2

    def goal_test(self, state):
        person = state[0]
        house = state[1]
        return person == house[:2]


if __name__ == "__main__":
    person = tuple(map(int, input().split(",")))
    inputs = tuple(map(int, input().split(",")))
    direction = input()
    if direction == "levo":
        house = (inputs[0], inputs[1], -1)
    else:
        house = (inputs[0], inputs[1], 1)
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]
    allowed = tuple(allowed)
    initial = (person, house)
    problem = Kacuvac(initial, allowed)
    solution = astar_search(problem)
    if solution is not None:
        print(solution.solution())
    else:
        print("[]")
