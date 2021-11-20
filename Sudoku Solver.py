"""
Sudoku solver
"""
Board = [
    [3, 0, 0, 8, 0, 1, 0, 0, 2],
    [2, 0, 1, 0, 3, 0, 6, 0, 4],
    [0, 0, 0, 2, 0, 4, 0, 0, 0],
    [8, 0, 9, 0, 0, 0, 1, 0, 6],
    [0, 6, 0, 0, 0, 0, 0, 5, 0],
    [7, 0, 2, 0, 0, 0, 4, 0, 9],
    [0, 0, 0, 5, 0, 9, 0, 0, 0],
    [9, 0, 4, 0, 8, 0, 7, 0, 5],
    [6, 0, 0, 1, 0, 7, 0, 0, 3]
]

def ValidSudoku(board):
    table = set()
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                num = str(board[i][j])
                if 'row' + str(j) + num in table:
                    return False
                else:
                    table.add('3' + str(j) + num)
                if 'column' + str(i) + num in table:
                    return False
                else:
                    table.add('column' + str(i) + num)
                if 'subgrid' + str((i - i % 3) + j // 3) + num in table:
                    return False
                else:
                    table.add('subgrid' + str((i - i % 3) + j // 3) + num)
    return True

def solve(board):
    i = 0
    stack = []
    while i < 9:
        j = 0
        while j < 9:
            if board[i][j] == 0 or (i, j) in stack:
                if not (i, j) in stack:
                    stack.append((i, j))
                x = board[i][j] + 1
                while not check(board, i, j, x) and x <= 9:
                    x += 1
                if x > 9:
                    board[i][j] = 0
                    stack.pop()
                    if len(stack) == 0:
                        return []
                    i = stack[-1][0]
                    j = stack[-1][1]
                    continue
                board[i][j] = x
            j += 1
        i += 1
    return board


def check(board, row, column, num):
    for i in range(9):
        if num == board[row][i]:
            return False
        if num == board[i][column]:
            return False
        if num == board[3 * (row // 3) + (i // 3)][3 * (column // 3) + (i % 3)]:
            return False
    return True

def displaySudoku(board):
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
    print("The Unsolved Sudoku: ")
    displaySudoku(Board)
    if ValidSudoku(Board):
        solution = solve(Board)
        if not solution:
            print("There is no solution!")
        else:
            print("\nThe Solved Sudoku: ")
            displaySudoku(solution)
    else:
        print("There is no solution!")

main()