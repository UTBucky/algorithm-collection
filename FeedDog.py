# Tallent 'Bucky' Hagan
# CS 325
# Homework 5

def feedDog(hunger_level, biscuit_size):
    """Greedy algorithm to calculate maximum numbers of dogs fed."""
    # Sort both lists in descending order
    hunger_level.sort(reverse=True)
    biscuit_size.sort(reverse=True)

    dogs_fed = 0
    biscuit_index = 0

    for level in hunger_level:
        if biscuit_size[biscuit_index] >= level:
            dogs_fed += 1
            biscuit_index += 1

    return dogs_fed
