from constraint import *


def max_4_po_termin(paper1, paper2, paper3, paper4, paper5, paper6, paper7, paper8, paper9, paper10):
    variables = [paper1, paper2, paper3, paper4, paper5, paper6, paper7, paper8, paper9, paper10]
    count_T1 = 0
    count_T2 = 0
    count_T3 = 0
    count_T4 = 0

    for variable in variables:
        if "T1" in variable:
            count_T1 += 1
        if "T2" in variable:
            count_T2 += 1
        if "T3" in variable:
            count_T3 += 1
        if "T4" in variable:
            count_T4 += 1
    return count_T1 <= 4 and count_T2 <= 4 and count_T3 <= 4 and count_T4 <= 4


if __name__ == '__main__':
    num = int(input())

    papers = dict()
    variables = []
    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite
    ai_papers = []
    ml_papers = []
    nlp_papers = []
    for item in papers:
        variables.append(f"{item} ({papers[item]})")
        if papers[item] == 'ML':
            ml_papers.append(f"{item} ({papers[item]})")
        if papers[item] == 'NLP':
            nlp_papers.append(f"{item} ({papers[item]})")
        if papers[item] == 'AI':
            ai_papers.append(f"{item} ({papers[item]})")
        # print(f"{item} ({papers[item]})")

    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranichuvanjata
    problem.addConstraint(max_4_po_termin, variables) # Najmn 4 trudovi po Termin

    # Vtoroto baranje da bidat prezentirani vo ist termin
    if 0 < len(ml_papers) <= 4:
        problem.addConstraint(AllEqualConstraint(), ml_papers)

    if 0 < len(nlp_papers) <= 4:
        problem.addConstraint(AllEqualConstraint(), nlp_papers)

    if 0 < len(ai_papers) <= 4:
        problem.addConstraint(AllEqualConstraint(), ai_papers)

    solution = problem.getSolution()

    names = sorted(solution)
    values = []
    for x in names:
        values.append(solution[x])

    print(f'{names[0]}: {values[0]}')
    for i in range(2, len(names)):
        print(f'{names[i]}: {values[i]}')
    print(f'{names[1]}: {values[1]}')
