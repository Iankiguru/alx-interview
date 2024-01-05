#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's triangle up to the nth row.
    """
    # Check if n is non-positive
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Populate the rest of the triangle
    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]

        # Generate the current row based on the previous row
        for j in range(1, i):
            row.append(prev_row[j-1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle
