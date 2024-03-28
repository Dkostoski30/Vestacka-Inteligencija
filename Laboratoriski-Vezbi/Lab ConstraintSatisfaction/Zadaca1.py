from constraint import *


def simona_termini(clen, vreme):
    if clen == 1:
        return vreme == 13 or vreme == 14 or vreme == 16 or vreme == 19
    else:
        return False


def petar_termini(clen, vreme):
    if clen == 1:
        return vreme == 12 or vreme == 13 or vreme == 16 or vreme == 17 or vreme == 18 or vreme == 19
    return True


def marija_termini(clen, vreme):
    if clen == 1:
        return vreme == 14 or vreme == 15 or vreme == 18
    else:
        return True


def barem1_prisuten(clen1, clen2):
    return clen1 == 1 or clen2 == 1


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Simona_prisustvo", [0, 1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", [13, 16, 19, 14])

    problem.addConstraint(simona_termini, ["Simona_prisustvo", "vreme_sostanok"])
    problem.addConstraint(petar_termini, ["Petar_prisustvo", "vreme_sostanok"])
    problem.addConstraint(marija_termini, ["Marija_prisustvo", "vreme_sostanok"])
    problem.addConstraint(barem1_prisuten, ["Petar_prisustvo", "Marija_prisustvo"])

    for solution in problem.getSolutions():
        print('{', end='')
        print(f"'Simona_prisustvo': {solution.get('Simona_prisustvo')}, ", end="")
        print(f"'Marija_prisustvo': {solution.get('Marija_prisustvo')}, ", end="")
        print(f"'Petar_prisustvo': {solution.get('Petar_prisustvo')}, ", end="")
        print(f"'vreme_sostanok': {solution.get('vreme_sostanok')}", end="")
        print('}')
