#!/usr/bin/python3

def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        prev_rowe = triangle[-1]
        row = [1]
        for j in range(1, i):
            row.append(prev_rowe[j-1] + prev_rowe[j])
        row.append(1)
        triangle.append(row)
    return triangle
