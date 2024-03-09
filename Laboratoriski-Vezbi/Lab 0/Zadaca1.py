import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"


class Student:
    def __init__(self, name, surname, index):
        self.name = name
        self.surname = surname
        self.index = index

    def __repr__(self):
        return name + " " + surname + " " + index


if __name__ == "__main__":
    students = dict()

    data = input()
    while data != "end":
        lines = data.split(",")
        name = lines[0]
        surname = lines[1]
        index = lines[2]
        student = (name, surname, index)
        subject = lines[3]
        teoretski_del = int(lines[4])
        prakticen_del = int(lines[5])
        labs = int(lines[6])
        ocenka = teoretski_del + prakticen_del + labs
        if 0 <= ocenka <= 50:
            ocenka = 5
        elif 50 < ocenka <= 60:
            ocenka = 6
        elif 60 < ocenka <= 70:
            ocenka = 7
        elif 70 < ocenka <= 80:
            ocenka = 8
        elif 80 < ocenka <= 90:
            ocenka = 9
        elif 90 < ocenka <= 100:
            ocenka = 10
        value = "----" + subject + ": " + str(ocenka)
        if student not in students:
            students[student] = {}
        students[student][subject] = ocenka
        data = input()

    for student, grades in students.items():
        print("Student: " + student[0] + " " + student[1])
        for subject, ocenka in grades.items():
            print(f"----{subject}: {ocenka}")
        print("")