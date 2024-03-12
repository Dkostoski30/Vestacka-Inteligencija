from searching_framework import Problem, breadth_first_graph_search, depth_limited_search


class Istrazuvac(Problem):
    def __init__(self, player, house):
        super().__init__((player, (2, 5, -1), (5, 0, 1)))
        self.house = house
        self.width = 8
        self.height = 7

    def successor(self, state):
        possible_moves = dict()
        actions = ['up', 'down', 'left', 'right']
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for action, direction in zip(actions, directions):
            new_state = self.move(state, direction)
            if new_state is not None:
                possible_moves[action] = new_state

        return possible_moves

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        player = state[0]
        return player == self.house

    def is_valid_state(self, state):
        player = state[0]
        if player[0] < 0 or player[0] >= self.width or player[1] < 0 or player[1] >= self.height:
            return False
        return True

    def move_player(self, player, direction):
        player = list(player)
        player[0] += direction[0]
        player[1] += direction[1]
        return tuple(player)

    def move_block(self, block):
        x, y, n = block
        y += n
        if y < 0 or y >= self.height:
            n *= -1
            y += 2 * n
        return x, y, n

    def move(self, state, direction):
        player = state[0]
        block_1 = state[1]
        block_2 = state[2]

        player = self.move_player(player, direction)
        block_1 = self.move_block(block_1)
        block_2 = self.move_block(block_2)

        new_state = (player, block_1, block_2)

        if self.is_valid_state(new_state):
            return new_state
        else:
            return None


if __name__ == "__main__":
    new_game = Istrazuvac((0, 0), (5, 5))
    node = breadth_first_graph_search(new_game)
    if node is not None:
        print(node.solution())
        print(node.solve())
        print(node.path())
    else:
        print("No solution found")
