from solvable import is_solvable
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
    #print(puzzle[i][j])
    return distance

# Testen der Funktion
# puzzle = [[1, 8, 2], [0, 4, 3], [7, 6, 5]]

# if is_solvable(puzzle):
#     print("Manhattan distance:", manhattan_distance(puzzle))
# else:
#     print("It is not solvable")

