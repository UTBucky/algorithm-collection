# Tallent 'Bucky' Hagan

def powerset(inputSet):
    """Returns a list of all subsets of the input set using backtracking."""
    result = []
    powerset_helper(len(inputSet)-1, [], inputSet, result)
    return result

def powerset_helper(pointer, choices_made, inputSet, result):
    if pointer < 0:
        result.append(choices_made.copy())
        return

    choices_made.append(inputSet[pointer])
    powerset_helper(pointer-1, choices_made, inputSet, result)

    choices_made.pop()
    powerset_helper(pointer-1, choices_made, inputSet, result)
