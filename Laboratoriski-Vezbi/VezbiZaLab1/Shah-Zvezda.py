from searching_framework import Problem, breadth_first_graph_search

class ShahZvezda(Problem):
    def __init__(self, lamfer, konj, zvezdi):
        super().__init__((lamfer, konj, zvezdi))
        self.number_of_zvezdi = len(zvezdi)
        self.width = 8

    def successor(self, state):
        pass

    def actions(self, state):
        pass

    def result(self, state, action):
        pass

    def is_move_valid(self, state):
        lamfer = state[0]
        konj = state[1]
        if lamfer[0] < 0 or konj[0] < 0:
            return False
        if lamfer[1] > self.width or lamfer[1] > self.width:
            return False
        if lamfer == konj:
            return False
        return True

    def move_konj(self, state, coordinates):
        konj = list(state[1])
        konj[0] += coordinates[0]
        konj[1] += coordinates[1]
        return tuple(konj)

    def move_lamfer(self, state, coordinates):
        lamfer = list(state[0])
        lamfer[0] += coordinates[0]
        lamfer[1] += coordinates[1]
        return tuple(lamfer)

    def move(self, state):
        pass

    def goal_test(self, state):
        return self.number_of_zvezdi == 0

