from searching_framework import Problem, uniform_cost_search

class Sadovi(Problem):
    def __init__(self, kapacitet, initial, goal):
        super().__init__(initial, goal)
        self.kapacitet = kapacitet

    def akcija_isturi(self, state, _od):
        if state[_od] == 0: return None

        nova_sostojba = list(state)
        nova_sostojba[_od] -= 1
        return tuple(nova_sostojba)
    def akcija_preturi(self, state, _od, _vo):
        if state[_od] == 0 or state[_vo] == self.kapacitet[_vo]: return None

        nova_sostojba = list(state)
        nova_sostojba[_od] -= 1
        nova_sostojba[_vo] += 1
        return tuple(nova_sostojba)

    def successor(self, state):
        sosedi = dict()
        rez1 = self.akcija_isturi(state, 0)
        if rez1 is not None: sosedi["Isturi od 0"] = rez1

        rez2 = self.akcija_isturi(state, 1)
        if rez2 is not None: sosedi["Isturi od 1"] = rez2

        rez3 = self.akcija_preturi(state, 0, 1)
        if rez3 is not None: sosedi["Preturi od 0 vo 1"] = rez3

        rez4 = self.akcija_preturi(state, 1, 0)
        if rez4 is not None: sosedi["Preturi od 1 vo 0"] = rez4

        return sosedi

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    kapaciteti = tuple(map(int, input().split()))
    goal_sostojba = tuple(map(int, input().split()))
    pocetna_sostojba = tuple(map(int, input().split()))
    problem = Sadovi(kapaciteti, pocetna_sostojba, goal_sostojba)
    node = uniform_cost_search(problem)
    print(node)
    if node is not None:
        print(node.solution())
        print(node.solve())
        print(node.path())
