#!/usr/bin/python3
"""
matrix island
"""

def island_perimeter(grid):
    """
    findig the perimwerter of island
    """
    def count_perimeter(r, c):
        perimeter = 0
        if r == 0 or grid[r - 1][c] == 0:
            perimeter += 1
        if r == len(grid) - 1 or grid[r + 1][c] == 0:
            perimeter += 1
        if c == 0 or grid[r][c - 1] == 0:
            perimeter += 1
        if c == len(grid[r]) - 1 or grid[r][c + 1] == 0:
            perimeter += 1
        return perimeter
    
    finalPerimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                finalPerimeter += count_perimeter(i, j)
    return finalPerimeter