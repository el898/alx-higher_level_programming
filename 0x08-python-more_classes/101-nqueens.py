#!/usr/bin/python3
"""N Queens Script"""


import sys

if __name__ == "__main__":

    arguments = sys.argv
    if (len(arguments) != 2):
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(arguments[1])
    except ValueError:
        n = ''

    if (not isinstance(n, int)):
        print("N must be a number")
        exit(1)

    if (n < 4):
        print("N must be at least 4")
        exit(1)

    solution_list = []
    n_arr = [[0]*n for _ in range(n)]

    def can_place(i, j):
        # if position has already been filled
        if (n_arr[i][j] == 1):
            return False

        if under_attack(i, j):
            return False

        return True

    def under_attack(i, j):
        # check row
        if 1 in n_arr[i]:
            return True

        # check column
        for k in range(n):
            if n_arr[k][j] == 1:
                return True

        # check diagonals
        ct = 1
        for m in range(i-1, -1, -1):
            if i < 0:
                break

            if (j-ct >= 0 and n_arr[m][j-ct] == 1):
                return True
            if (j+ct < n and n_arr[m][j+ct] == 1):
                return True

            ct += 1

        ct = 1
        for m in range(i+1, n):
            if i < 0:
                break

            if (j-ct >= 0 and n_arr[m][j-ct] == 1):
                return True
            if (j+ct < n and n_arr[m][j+ct] == 1):
                return True
            ct += 1

        return False

    def print_final_result():
        # print solutions
        for s in solution_list:
            final_solution = []
            for i in range(n):
                for j in range(n):
                    if (s[i][j] == 1):
                        final_solution.append([i, j])
            print(final_solution)

    def nqueens(i):
        if i == n:
            solution_list.append([list(i) for i in n_arr])
            return True

        for j in range(n):
            if can_place(i, j):
                n_arr[i][j] = 1
                nqueens(i+1)
                n_arr[i][j] = 0

    nqueens(0)
    print_final_result()
