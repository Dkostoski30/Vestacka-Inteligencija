from constraint import *


def ML_razlTermin(predavanja_termin, vezbi_termin):
    return predavanja_termin[-2:] != vezbi_termin[-2:]


#  ["AI_cas_1", "ML_cas_1", "R_cas_1", "BI_cas_1", "ML_vezbi", "AI_vezbi", "BI_vezbi"]
def termin_2h(termin1, termin2):
    if termin1[:4] == termin2[:4]:
        termin1 = int(termin1[-2:])
        termin2 = int(termin2[-2:])
        return abs(termin1 - termin2) > 1

    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = int(input())
    casovi_ML = int(input())
    casovi_R = int(input())
    casovi_BI = int(input())

    AI_casovi = []
    ML_casovi = []
    R_casovi = []
    BI_casovi = []

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Tuka dodadete gi promenlivite--------------------

    for i in range(casovi_AI):
        AI_casovi.append(f"AI_cas_{i+1}")
    for i in range(casovi_ML):
        ML_casovi.append(f"ML_cas_{i+1}")
    for i in range(casovi_R):
        R_casovi.append(f"R_cas_{i+1}")
    for i in range(casovi_BI):
        BI_casovi.append(f"BI_cas_{i+1}")

    problem.addVariables(AI_casovi, AI_predavanja_domain)
    problem.addVariables(ML_casovi, ML_predavanja_domain)
    problem.addVariables(R_casovi, R_predavanja_domain)
    problem.addVariables(BI_casovi, BI_predavanja_domain)

    problem.addVariable("AI_vezbi", AI_vezbi_domain)
    problem.addVariable("BI_vezbi", BI_vezbi_domain)
    problem.addVariable("ML_vezbi", ML_vezbi_domain)
    site_casovi = AI_casovi + BI_casovi +ML_casovi + R_casovi + ["AI_vezbi", "ML_vezbi", "BI_vezbi"]
    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(AllDifferentConstraint(), site_casovi)
    site_ML_casovi = ML_casovi + ["ML_vezbi"]
    for termin1 in site_ML_casovi:
        for termin2 in site_ML_casovi:
            if termin1 != termin2:
                problem.addConstraint(ML_razlTermin, [termin1, termin2])

    for termin1 in site_casovi:
        for termin2 in site_casovi:
            if termin1 != termin2:
                problem.addConstraint(termin_2h, [termin1, termin2])

    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)
