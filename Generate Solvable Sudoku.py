# Generate a sudoku puzzle with at least one solution
# By creating a solved one first and removing parts of it
# Might take up to 3 seconds to generate one
from random import *


def rand(n=""):
    # generate a integer from 1 to 9 except any from set n
    r = randint(1, 9)
    return r if str(r) not in n else rand(n)


def generate_solution():
    board = [[0 for z in range(9)] for z in range(9)]
    i = 0
    while i < 9:
        j = 0
        while j < 9:
            x = rand()
            s = str(x)
            while not check(board, i, j, x) and len(s) < 9:
                x = rand(s)
                s += str(x)
            if len(s) >= 9:
                board[i][j] = 0
                j -= 1
                if randint(0,100) == 69:
                    # This line is necessary
                    board[i] = [0 for g in range(9)]
                    i -= 1
                if j < 0:
                    i, j = i - 1, 8
                if i < 0:
                    i = j = 0
                continue
            board[i][j] = x
            j += 1
        i += 1
    return board


def generate_puzzle(s):
    puzzle = [[digit for digit in line] for line in s]
    for i in range(9):
        for j in range(9):
            if randint(0, 29) < 15:
                puzzle[i][j] = 0
    return puzzle


def check(board, row, column, num):
    for i in range(9):
        if num == board[row][i]:
            return False
        if num == board[i][column]:
            return False
        if num == board[3 * (row // 3) + (i // 3)][3 * (column // 3) + (i % 3)]:
            return False
    return True


def display_sudoku(board):
    for i in range(9):
        s = ""
        if i % 3 == 0 and i != 0:
            q = '— ' * 3
            print(f"{q}+ {q}+ {q}")
        for j in range(9):
            if board[i][j] == 0:
                s += "x "
            else:
                s += str(board[i][j]) + ' '
            if j % 3 == 2 and j != 8:
                s += '| '
        print(s)


def main():
    solution = generate_solution()
    puzzle = generate_puzzle(solution)
    print("The puzzle:")
    display_sudoku(puzzle)
    print("\nThe solution: ")
    display_sudoku(solution)

main()


