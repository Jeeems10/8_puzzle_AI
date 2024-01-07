# solver.py
import heapq

from setuptools.namespaces import flatten

from solvable import is_solvable

GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


class PuzzleState:

    # constructor
    def __init__(self, state):
        self.state = state

    # equal states
    def __eq__(self, other):
        return self.state == other.state

    # non equal states
    def __ne__(self, other):
        return not self.__eq__(other)

    # gives each state a hash
    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.state))

    # puts puzzle states in order
    def __lt__(self, other):
        return self.state < other.state


def hamming_heuristic(current_state):
    flattened_current = flatten(current_state.state)
    # sums up True values --> True = misplaced
    misplaced_tiles = sum(current != goal for current, goal in zip(flattened_current, flatten(GOAL_STATE)))

    return misplaced_tiles


def generate_neighbors(state):
    neighbors = []
    zero_row, zero_col = find_zero_position(state.state)

    # Move the blank tile (zero) to the left
    if zero_col > 0:
        neighbor = swap(state.state, zero_row, zero_col, zero_row, zero_col - 1)
        neighbors.append(PuzzleState(neighbor))

    # Move the blank tile to the right
    if zero_col < 2:
        neighbor = swap(state.state, zero_row, zero_col, zero_row, zero_col + 1)
        neighbors.append(PuzzleState(neighbor))

    # Move the blank tile upward
    if zero_row > 0:
        neighbor = swap(state.state, zero_row, zero_col, zero_row - 1, zero_col)
        neighbors.append(PuzzleState(neighbor))

    # Move the blank tile downward
    if zero_row < 2:
        neighbor = swap(state.state, zero_row, zero_col, zero_row + 1, zero_col)
        neighbors.append(PuzzleState(neighbor))

    return neighbors


def find_zero_position(state):
    for i, row in enumerate(state):
        for j, value in enumerate(row):
            if value == 0:
                return i, j


def swap(state, row1, col1, row2, col2):
    new_state = [row.copy() for row in state]
    new_state[row1][col1], new_state[row2][col2] = new_state[row2][col2], new_state[row1][col1]
    return new_state


def manhattan_distance(puzzle):
    distance = 0
    size = len(puzzle)  # Größe des 2 dimensionalen Puzzles ist 3
    for i in range(size):
        for j in range(size):
            if puzzle[i][j] != 0:  # Ignoriert 0

                # Zielposition der aktuellen Zahl finden
                x, y = divmod(puzzle[i][j] - 1, size)
                # Distanz zur Zielposition addieren
                distance += abs(x - i) + abs(y - j)

    return distance


def a_star(initial_state, heuristic):
    heap = [(0, PuzzleState(initial_state), [])]
    visited = set()

    while heap:
        cost, current_state, path = heapq.heappop(heap)

        if current_state.state == GOAL_STATE:
            return True, path

        # avoid revisiting states
        if current_state in visited:
            continue

        # adds current state to visited
        visited.add(current_state)

        # expand current state and add neighbors to the priority queue
        for neighbor in generate_neighbors(current_state):
            neighbor_cost = cost + 1
            priority = neighbor_cost + heuristic(neighbor)
            heapq.heappush(heap, (priority, neighbor, path + [(current_state, neighbor)]))

    return False, []


def manhattan_heuristic(state):
    return manhattan_distance(state.state)
