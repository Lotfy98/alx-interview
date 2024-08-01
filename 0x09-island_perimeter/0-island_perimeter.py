#!/usr/bin/python3
"""Island Perimeter Problem
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid
    Args:
        grid: 2d list of integers containing 0(water) or 1(land)
    Return:
        the perimeter of the island
    """

    per = 0
    for i in range(len(grid)):
        for e in range(len(grid[i])):
            if (grid[i][e] == 1):
                if (i <= 0 or grid[i - 1][e] == 0):
                    per += 1
                if (i >= len(grid) - 1 or grid[i + 1][e] == 0):
                    per += 1
                if (e <= 0 or grid[i][e - 1] == 0):
                    per += 1
                if (e >= len(grid[i]) - 1 or grid[i][e + 1] == 0):
                    per += 1
    return per
