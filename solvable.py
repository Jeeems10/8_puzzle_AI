def count_inversions(puzzle):
    inversions = 0

    #ich wandle das 2 Dimensionale Array in ein 1 Dimensionales Array und füge alles der Liste hinzu außer die Zahl 0 -j
    liste_puzzel = []
    for row in puzzle:
        for num in row:
            if num != 0:
                liste_puzzel.append(num)

    #ist eine verschachtelte Liste, wo ich die äußere Schleife mit der Inneren Schleife vergleiche -j
    for i in range(len(liste_puzzel)):
        for j in range(i + 1, len(liste_puzzel)):
            if liste_puzzel[i] > liste_puzzel[j]:
                inversions += 1
    return inversions

def is_solvable(puzzle):
    #wenn die Inversion gerade ist, dann ist das Puzzle Lösbar-j
    return count_inversions(puzzle) % 2 == 0

# Beispiel für ein puzzle
puzzle = [[1, 8, 2], [0, 4, 3], [7, 6, 5]]

#testen
if is_solvable(puzzle):
    print("Yes, the puzzle is solvable")
else:
    print("It is not solvable")



