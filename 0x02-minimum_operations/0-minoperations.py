#!/usr/bin/python3
"""
Calculates the fewest number of operations to achieve a given number of 'H' characters in a text file.
"""

def min_operations(n):
    """
    Calculates the fewest number of operations to achieve a given number of 'H' characters.

    Args:
    - n (int): The target number of 'H' characters.

    Returns:
    - int: The minimum number of operations required.
    """
    if n <= 1:
        return 0

    operations = 0
    current_length = 1
    clipboard = 1

    while current_length < n:
        if n % current_length == 0:
            clipboard = current_length
            operations += 1

        current_length += clipboard
        operations += 1

    return operations

if __name__ == "__main__":
    # Test cases
    n1 = 4
    print(f"Min # of operations to reach {n1} char: {min_operations(n1)}")

    n2 = 12
    print(f"Min # of operations to reach {n2} char: {min_operations(n2)}")

