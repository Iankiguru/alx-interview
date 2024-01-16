#!/usr/bin/python3
"""
Main file for testing
"""

min_operations = __import__('0-minoperations').min_operations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
