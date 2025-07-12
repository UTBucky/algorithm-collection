# Tallent 'Bucky' Hagan

from collections import deque

def solve_puzzle(Board, Source, Destination):
    source_x, source_y = Source
    destination_x, destination_y = Destination

    if (source_x, source_y) == (destination_x, destination_y):
        return [(source_x, source_y)]

    rows = len(Board)
    cols = len(Board[0])

    cells_visited = [[False] * cols for _ in range(rows)]
    cells_visited[source_x][source_y] = True

    cell_queue = deque([(source_x, source_y)])
    tracking_dictionary = {}
    path_to_destination = []

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while cell_queue:
        current_row, current_col = cell_queue.popleft()

        for x, y in directions:
            new_row, new_col = current_row + x, current_col + y

            if 0 <= new_row < rows and 0 <= new_col < cols and Board[new_row][new_col] != '#' and not cells_visited[new_row][new_col]:
                cells_visited[new_row][new_col] = True
                cell_queue.append((new_row, new_col))
                tracking_dictionary[(new_row, new_col)] = (current_row, current_col)

                if (new_row, new_col) == (destination_x, destination_y):
                    cell_key = (new_row, new_col)
                    while cell_key != (source_x, source_y):
                        path_to_destination.append(cell_key)
                        cell_key = tracking_dictionary[cell_key]
                    path_to_destination.append((source_x, source_y))
                    path_to_destination.reverse()

                    return path_to_destination

    # Return none if the queue becomes empty before reaching destination cell
    return None

