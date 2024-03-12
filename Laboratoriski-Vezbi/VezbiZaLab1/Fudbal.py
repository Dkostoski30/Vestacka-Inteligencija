from searching_framework import Problem, breadth_first_graph_search


class Fudbal(Problem):
    def __init__(self, initial, obstacles, goal):
        # state ((igrac, topka))
        super().__init__(initial)
        self.obstacles = obstacles
        self.goal = goal
        self.height = 6
        self.width = 8

    def successor(self, state):
        igrac = list(state[0])
        topka = list(state[1])
        possible_moves = dict()
        akcii = ["gore", "dolu", "desno", "gore-desno", "dolu-desno"]
        directions = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1)]
        for direction, action in zip(directions, akcii):
            new_state = self.pomesti_igrac(state, direction)
            if self.check_valid(new_state):
                possible_moves[f"Pomesti coveche {direction}"] = new_state
        return possible_moves

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        topka = state[1]
        return topka in self.goal

    def check_valid(self, state):
        topka = state[1]
        igrac = state[0]

        if igrac in self.obstacles:
            return False
        if igrac == topka:
            return False
        if topka in self.obstacles:
            return False
        for obstacle in self.obstacles:
            if manhattan_distance(topka, obstacle) < 3:
                return False
        if topka[0] >= self.width or topka[1] >= self.height:
            return False
        if igrac[0] >= self.width or igrac[1] >= self.height:
            return False
        if igrac[0] < 0 or igrac[1] < 0:
            return False
        if topka[0] < 0 or topka[1] < 0:
            return False
        return True

    def pomesti_igrac(self, state, direction):
        igrac = list(state[0])
        igrac[0] += direction[0]
        igrac[1] += direction[1]
        topka = state[1]
        igrac = tuple(igrac)
        topka = tuple(topka)
        return igrac, topka

    def sutni_topka(self, state, direction):
        igrac = list(state[0])
        topka = list(state[1])
        topka[0] += direction[0]
        topka[1] += direction[1]
        igrac = tuple(igrac)
        topka = tuple(topka)
        return igrac, topka


def manhattan_distance(point1, point2):
    point1 = (int(point1[0]), int(point1[1]))
    point2 = (int(point2[0]), int(point2[1]))
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)


if __name__ == '__main__':
    player_position = tuple(input().split(","))
    player_position = (int(player_position[0]), int(player_position[1]))
    ball_position = tuple(input().split(","))
    ball_position = (int(ball_position[0]), int(ball_position[1]))
    opponent_position = ((3, 3), (5, 4))
    goal_position = ((7, 2), (7, 3))
    match = Fudbal((player_position, ball_position), opponent_position, goal_position)
    print(breadth_first_graph_search(match).solution())
