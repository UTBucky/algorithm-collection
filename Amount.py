# Tallent 'Bucky' Hagan
# CS 325
# Homework 5

from copy import deepcopy

def amount_helper(A, start, result, remain, combo):
    """Recursive helper function to find all unique combos for a target sum."""
    # Base case
    if remain == 0:
        if combo not in result:
            result.append(deepcopy(combo))
        return
    if remain < 0:
        return

    for i in range(start, len(A)):
        combo.append(A[i])
        amount_helper(A, i + 1, result, remain - A[i], combo)
        combo.pop()

def amount(A, S):
    A.sort()
    result = []
    amount_helper(A, 0, result, S, [])
    return result
