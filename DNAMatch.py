# Tallent 'Bucky' Hagan

def dna_match_topdown(dna_string1, dna_string2):
    """
    Performs a top-down approach to calculate the longest common
    string alignment between two DNA sequence strings.
    :param dna_string1: a string
    :param dna_string2: a string
    :return: an integer representing the longest common string alignment
    """
    string1_length = len(dna_string1)
    string2_length = len(dna_string2)

    # 2D Array to hold previously calculated values
    cache = [[0] * string2_length for _ in range(string1_length + 1)]

    # Calls the recursive helper function
    return dna_match_topdown_helper(dna_string1, dna_string2, string1_length-1, string2_length-1, cache)


def dna_match_topdown_helper(dna_string1, dna_string2, index1, index2, cache):

    # Base case
    if index1 == -1 or index2 == -1:
        return 0

    # Returns values for already calculated sub-problems
    if cache[index1][index2] != 0:
        return cache[index1][index2]

    # Matching characters adds 1 to the value in corresponding 2D array index
    if dna_string1[index1] == dna_string2[index2]:
        cache[index1][index2] = 1 + dna_match_topdown_helper(dna_string1, dna_string2, index1-1, index2-1, cache)

    # Looks for the max value between [index1][index2-1] and [index1-1][index2] when characters do not match
    if dna_string1[index1] != dna_string2[index2]:
        cache[index1][index2] = max(dna_match_topdown_helper(dna_string1, dna_string2, index1, index2-1, cache),
                                    dna_match_topdown_helper(dna_string1, dna_string2, index1-1, index2, cache))

    return cache[index1][index2]


def dna_match_bottomup(dna_string1, dna_string2):
    """
    Performs a bottom-up approach to find the longest common
    string alignment for two DNA sequence strings.
    :param dna_string1: a string
    :param dna_string2: a string
    :return: an integer representing the longest common string alignment
    """
    string1_length = len(dna_string1)
    string2_length = len(dna_string2)

    # 2D Array to hold values for longest subsequence
    cache = [[0] * (string2_length + 1) for _ in range(string1_length + 1)]

    for i in range(1, string1_length + 1):

        for j in range(1, string2_length + 1):

            # Matching characters adds 1 to the value in corresponding 2D array index
            if dna_string1[i - 1] == dna_string2[j - 1]:
                cache[i][j] = cache[i - 1][j - 1] + 1

            # Looks for the max value between [index1][index2-1] and [index1-1][index2] when characters do not match
            else:
                cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])

    return cache[string1_length][string2_length]
