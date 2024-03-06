from searching_framework import Problem, breadth_first_graph_search, depth_first_graph_search, \
    greedy_best_first_graph_search


class Istrazuvac(Problem):
    def __init__(self, person, house):
        super().__init__((person, (2, 5, -1), (5, 0, +1)))
        self.house = house
        self.rows = 6
        self.cols = 8

    def goal_test(self, state):
        person = state[0]
        return person == self.house

    def successor(self, state):
        sosedi = dict()
        akcii = ("Desno", "Levo", "Gore", "Dolu")
        nasoki = ((+1, 0), (-1, 0), (0, +1), (0, -1))

        for akcija, nasoka in zip(akcii, nasoki):
            rez = self.akcija_dvizi(state, nasoka)
            if rez is not None: sosedi[akcija] = rez

        return sosedi

    def actions(self, state):
            return self.successor(state).keys()

    def result(self, state, action):
            return self.successor(state)[action]

    def akcija_dvizi(self, state, nasoka):
        istrazuvac = self.akcija_dvizi_istrazuvac(state[0], nasoka)
        blok_1 = self.akcija_dvizi_blok(state[1])
        blok_2 = self.akcija_dvizi_blok(state[2])

        nova_sostojba = (istrazuvac, blok_1, blok_2)
        if self.proverka_validnost(nova_sostojba):
            return tuple(nova_sostojba)
        else:
            return None
    def akcija_dvizi_istrazuvac(self, state, nasoka):
        # nasoka e vo format (x, y)
        # x/y edinici dvizi se
        istrazuvac = list(state)
        istrazuvac[0] += nasoka[0]
        istrazuvac[1] += nasoka[1]
        return tuple(istrazuvac)

    def akcija_dvizi_blok(self, block):
        x, y, n = block
        y += n
        if y < 0 or y >= self.rows:
            n *= -1
            y += 2 * n
        return x, y, n

    def proverka_validnost(self, state):
        istrazuvac, blok1, blok2 = state
        ist_x, ist_y = istrazuvac
        if 0 <= ist_x < self.cols and 0 <= ist_y < self.rows and istrazuvac != blok1[:2] and istrazuvac != blok2[:2]:
            return True
        else:
            return False


if __name__ == '__main__':
    person = tuple(map(int, input().split()))
    house = tuple(map(int, input().split()))
    problem = Istrazuvac(person, house)
    node = breadth_first_graph_search(problem)
    if node is not None:
        print(node.solution())
        print(node.solve())
        print(node.path())
    else:
        print("Nemat Resenie")
