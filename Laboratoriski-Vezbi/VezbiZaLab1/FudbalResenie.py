from searching_framework import Problem, breadth_first_graph_search


def validacija_na_sostojba(state, obstacles):
    igrac = tuple(state[0])
    topka = tuple(state[1])

    if igrac == topka:
        return False
    if igrac[0] < 0 or igrac[1] < 0 or igrac[0] >= 8 or igrac[1] >= 6:
        return False
    if topka[0] < 0 or topka[1] < 0 or topka[0] >= 8 or topka[1] >= 6:
        return False
    if topka in obstacles:
        return False
    if igrac in ((3, 3), (5, 4)):
        return False

    return True


def pomesti_coveche_gore(state, obstacles):
    igrac = list(state[0])
    topka = state[1]
    igrac[1] += 1
    igrac = tuple(igrac)
    topka = tuple(topka)
    new_state = (igrac, topka)
    if validacija_na_sostojba(new_state, obstacles):
        return new_state
    else:
        return state


def pomesti_coveche_dolu(state, obstacles):
    igrac = list(state[0])
    topka = state[1]

    igrac[1] -= 1
    igrac = tuple(igrac)
    topka = tuple(topka)
    new_state = (igrac, topka)
    if validacija_na_sostojba(new_state, obstacles):
        return new_state
    else:
        return state


def pomesti_coveche_desno(state, obstacles):
    igrac = list(state[0])
    topka = state[1]
    igrac[0] += 1
    igrac = tuple(igrac)
    topka = tuple(topka)
    new_state = (igrac, topka)
    if validacija_na_sostojba(new_state, obstacles):
        return new_state
    else:
        return state


def pomesti_coveche_goreDesno(state, obstacles):
    igrac = list(state[0])
    topka = state[1]
    igrac[0] += 1
    igrac[1] += 1
    igrac = tuple(igrac)
    topka = tuple(topka)
    new_state = (igrac, topka)
    if validacija_na_sostojba(new_state, obstacles):
        return new_state
    else:
        return state


def pomesti_coveche_doluDesno(state, obstacles):
    igrac = list(state[0])
    topka = state[1]
    igrac[0] += 1
    igrac[1] -= 1
    igrac = tuple(igrac)
    topka = tuple(topka)
    new_state = (igrac, topka)
    if validacija_na_sostojba(new_state, obstacles):
        return new_state
    else:
        return state


def turni_topka_desno(state, obstacles):
    igrac = list(state[0])
    topka = list(state[1])
    if igrac[0] + 1 == topka[0] and igrac[1] == topka[1]:
        topka[0] += 1
        igrac = tuple(igrac)
        topka = tuple(topka)
        new_state = (igrac, topka)
        new_state = pomesti_coveche_desno(new_state, obstacles)
        if validacija_na_sostojba(new_state, obstacles):
            return new_state
        else:
            return state
    else:
        return state


def turni_topka_gore(state, obstacles):
    igrac = list(state[0])
    topka = list(state[1])
    if igrac[0] == topka[0] and igrac[1] + 1 == topka[1]:
        topka[1] += 1
        igrac = tuple(igrac)
        topka = tuple(topka)
        new_state = (igrac, topka)
        new_state = pomesti_coveche_gore(new_state, obstacles)
        if validacija_na_sostojba(new_state, obstacles):
            return new_state
        else:
            return state
    else:
        return state


def turni_topka_dolu(state, obstacles):
    igrac = list(state[0])
    topka = list(state[1])
    if igrac[0] == topka[0] and igrac[1] - 1 == topka[1]:
        topka[1] -= 1
        igrac = tuple(igrac)
        topka = tuple(topka)
        new_state = (igrac, topka)
        new_state = pomesti_coveche_dolu(new_state, obstacles)
        if validacija_na_sostojba(new_state, obstacles):
            return new_state
        else:
            return state
    else:
        return state


def turni_topka_doluDesno(state, obstacles):
    igrac = list(state[0])
    topka = list(state[1])
    if igrac[0] + 1 == topka[0] and igrac[1] - 1 == topka[1]:
        topka[1] -= 1
        topka[0] += 1
        igrac = tuple(igrac)
        topka = tuple(topka)
        new_state = (igrac, topka)
        new_state = pomesti_coveche_doluDesno(new_state, obstacles)
        if validacija_na_sostojba(new_state, obstacles):
            return new_state
        else:
            return state
    else:
        return state


def turni_topka_goreDesno(state, obstacles):
    igrac = list(state[0])
    topka = list(state[1])
    if igrac[0] + 1 == topka[0] and igrac[1] + 1 == topka[1]:
        topka[1] += 1
        topka[0] += 1
        igrac = tuple(igrac)
        topka = tuple(topka)
        new_state = (igrac, topka)
        new_state = pomesti_coveche_goreDesno(new_state, obstacles)
        if validacija_na_sostojba(new_state, obstacles):
            return new_state
        else:
            return state
    else:
        return state


class Fudbal(Problem):
    # state(igrac, topka)
    def __init__(self, initial, obstacles, gol, goal=None):
        super().__init__(initial, goal)
        self.obstacles = obstacles
        self.gol = gol

    def successor(self, state):
        possible_moves = dict()

        new_state = pomesti_coveche_desno(state, self.obstacles)
        if new_state != state:
            possible_moves["Pomesti coveche desno"] = new_state

        new_state = pomesti_coveche_gore(state, self.obstacles)
        if new_state != state:
            possible_moves["Pomesti coveche gore"] = new_state

        new_state = pomesti_coveche_dolu(state, self.obstacles)
        if new_state != state:
            possible_moves["Pomesti coveche dolu"] = new_state

        new_state = pomesti_coveche_doluDesno(state, self.obstacles)
        if new_state != state:
            possible_moves["Pomesti coveche dolu-desno"] = new_state

        new_state = pomesti_coveche_goreDesno(state, self.obstacles)
        if new_state != state:
            possible_moves["Pomesti coveche gore-desno"] = new_state

        # sega za topkata
        new_state = turni_topka_desno(state, self.obstacles)
        if new_state != state:
            possible_moves["Turni topka desno"] = new_state

        new_state = turni_topka_gore(state, self.obstacles)
        if new_state != state:
            possible_moves["Turni topka gore"] = new_state

        new_state = turni_topka_dolu(state, self.obstacles)
        if new_state != state:
            possible_moves["Turni topka dolu"] = new_state

        new_state = turni_topka_goreDesno(state, self.obstacles)
        if new_state != state:
            possible_moves["Turni topka gore-desno"] = new_state

        new_state = turni_topka_doluDesno(state, self.obstacles)
        if new_state != state:
            possible_moves["Turni topka dolu-desno"] = new_state

        return possible_moves

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        topka = tuple(state[1])
        return topka in self.gol


if __name__ == "__main__":
    igrac = tuple(map(int, input().split(",")))
    topka = tuple(map(int, input().split(",")))
    obstacles = ((2, 2), (3, 2), (4, 2), (2, 3), (4, 3), (5, 3), (6, 3),
                 (2, 4), (3, 4), (4, 4), (6, 4),
                 (4, 5), (5, 5), (6, 5))
    gol = ((7, 2), (7, 3))
    problem = Fudbal((igrac, topka), obstacles, gol)
    solution = breadth_first_graph_search(problem)
    if solution is not None:
        print(solution.solution())
    else:
        print("[]")
