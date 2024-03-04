#!/usr/bin/python3
"""
island perimeter
"""


def island_perimeter(grid):
    """
     returns the perimeter of the island described in grid
    """
    lenRow = len(grid)
    lenCol = len(grid[0])
    perim = 0
    connections = 0

    for x in range(0, lenRow):
        for y in range(0, lenCol):
            if grid[x][y] == 1:
                perim += 4
                if x != 0 and grid[x - 1][y] == 1:
                    connections += 1
                if y != 0 and grid[x][y - 1] == 1:
                    connections += 1
    return perim - (connections * 2)
