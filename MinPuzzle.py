# Tallent 'Bucky' Hagan

import heapq

def minEffort(puzzle):
    rows = len(puzzle)
    cols = len(puzzle[0])

    effort_memo = [[float('inf')] * cols for _ in range(rows)]
    effort_memo[0][0] = 0

    pq = [(0, 0, 0)]

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while len(pq) > 0:
        current_effort, current_row, current_col = heapq.heappop(pq)

        if current_row == rows - 1 and current_col == cols - 1:
            return current_effort

        for x, y in directions:
            new_row, new_col = current_row + x, current_col + y

            if 0 <= new_row < rows and 0 <= new_col < cols:
                new_effort = max(current_effort, abs(puzzle[current_row][current_col] - puzzle[new_row][new_col]))

                if new_effort < effort_memo[new_row][new_col]:
                    effort_memo[new_row][new_col] = new_effort
                    heapq.heappush(pq, (new_effort, new_row, new_col))




