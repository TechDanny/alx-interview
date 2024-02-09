#!/usr/bin/python3
"""
N queens
"""


import sys


solutions = []
n = 0
position = None


def get_input():
    """
    Returns the size of the board
    """
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_striking(position0, position1):
    """
    returns a boolean
    """
    if (position0[0] == position1[0]) or (position0[1] == position1[1]):
        return True
    return abs(position0[0] - position1[0]) == abs(position0[1] - position1[1])


def exists(member):
    """
    returns a boolean
    """
    global solutions
    for sol in solutions:
        i = 0
        for y in sol:
            for x in member:
                if y[0] == x[0] and y[1] == x[1]:
                    i += 1
        if i == n:
            return True
    return False


def built_in(row, group):
    """
    
    """
    global solutions
    global n
    if row == n:
        tmp0 = group.copy()
        if not exists(tmp0):
            solutions.append(tmp0)
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip(list([position[a]]) * len(group), group)
            used_positions = map(lambda x: is_striking(x[0], x[1]), matches)
            group.append(position[a].copy())
            if not any(used_positions):
                built_in(row + 1, group)
            group.pop(len(group) - 1)


def get_solutions():
    """Gets the solutions for the given chessboard size.
    """
    global position, n
    position = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    a = 0
    group = []
    built_in(a, group)


n = get_input()
get_solutions()
for solution in solutions:
    print(solution)