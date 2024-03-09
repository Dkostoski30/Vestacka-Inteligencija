import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"

def count_mines(matrix, i, j):
    counter = 0
    for k in range(-1, 2):
        for m in range(-1, 2):
            if 0 <= i + k < len(matrix) and 0 <= j + m < len(matrix[0]) and matrix[i + k][j + m] == '#':
                counter += 1
    return counter

def minesweeper(minefield, n):
    result = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if minefield[i][j] == '-':
                result[i][j] = count_mines(minefield, i, j)
            else:
                result[i][j] = "#"
    return result

if __name__ == "__main__":
    n = int(input())
    minefield = []
    for i in range(n):
        minefield.append(input())

    for i in range(n):
        minefield[i] = minefield[i].split("   ")

    result = minesweeper(minefield, n)

    for i in range(len(result)):
        for j in range(len(result[i])):
            if j != 0:
                print(f"  {result[i][j]}", end=" ")
            else:
                print(f"{result[i][j]}", end=" ")
        print()
