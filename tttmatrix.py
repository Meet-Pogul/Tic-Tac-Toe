import numpy as np

times = 0


def printMatrix(matrix):
    for i in matrix:
        for j in i:
            print(f"|{j}|", end="")
        print()


def win(player):
    print(f"Player {player.upper()} Won")
    exit()


def check(matrix):
    global times
    a, b = np.diag(matrix), np.fliplr(matrix).diagonal()
    if np.all(a != ' ') and np.all(a == a[0]):
        printMatrix(matrix)
        win(a[0])
    if np.all(b != ' ') and np.all(b == b[0]):
        printMatrix(matrix)
        win(b[0])
    for i in matrix:
        if np.all(i != ' ') and np.all(i == i[0]):
            printMatrix(matrix)
            win(i[0])
    for i in matrix.T:
        if np.all(i != ' ') and np.all(i == i[0]):
            printMatrix(matrix)
            win(i[0])


def result(matrix, curr):
    try:
        a, b = int(curr[0]), int(curr[1])
        if matrix[a, b] == ' ':
            matrix[a, b] = curr[2]
        else:
            print("Cannot Overrite")
            global times
            times -= 1
        check(matrix)
    except Exception:
        print("Invalid Input")
    return matrix


def getcurrList(pos):
    global times
    curr = []
    if pos < 0:
        return [None]
    elif pos < 3:
        curr.extend([0, pos])
    elif pos < 6:
        curr.extend([1, pos-3])
    elif pos < 9:
        curr.extend([2, pos-6])
    if times % 2 == 0:
        curr.append('o')
    else:
        curr.append('x')
    times += 1
    return curr


if __name__ == "__main__":
    matrix = np.zeros((3, 3), dtype='object')
    matrix.fill(' ')
    printMatrix(matrix)
    while times < 9:
        try:
            pos = int(input("Enter: "))
        except ValueError:
            print("Invalid Input")
            continue
        pos -= 1
        matrix = result(matrix, getcurrList(pos))
        printMatrix(matrix)
    else:
        print("It's Tie")
