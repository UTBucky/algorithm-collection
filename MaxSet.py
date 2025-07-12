# Tallent 'Bucky' Hagan

def max_independent_set(nums):
    """Finds the maximum sum of non-consecutive integers in an array."""
    if len(nums) == 0:
        return [0]

    # Checks for input list with all negative numbers
    negative_flag = True
    for i in range(len(nums)):
        if nums[i] >= 0:
            negative_flag = False
            break

    if negative_flag:
        return []

    max_sum_arr = [0] * len(nums)

    # Set base cases
    max_sum_arr[0] = max(0, nums[0])
    if len(nums) > 1:
        max_sum_arr[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        max_sum_arr[i] = max(max_sum_arr[i - 1], nums[i] + max_sum_arr[i - 2])

    non_consecutive_number_arr = []

    # Initialize loop to end of array which holds maximum sum
    index = len(nums) - 1

    while index >= 0:
        if nums[index] <= 0:
            index -= 1
        elif max_sum_arr[index] != max_sum_arr[index - 1] or index == 0:
            non_consecutive_number_arr.append(nums[index])
            index -= 2
        else:
            index -= 1

    return non_consecutive_number_arr
