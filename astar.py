graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
    'J': [('E', 5), ('I', 3)]
}

heuristic = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 3,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 1,
    'J': 0
}


def astar(mulai, tujuan, graf, heuristik):
    perbatasan = [(heuristik[mulai] + 0, 0, mulai, [])]
    sudah_dieksplore = set()

    while perbatasan:
        perbatasan.sort(reverse=True)
        (priority, biaya_sejauh_ini, sekarang, jalur) = perbatasan.pop()

        if sekarang == tujuan:
            return jalur + [sekarang]

        if sekarang not in sudah_dieksplore:
            print(f"Memilih simpul {sekarang} dengan prioritas {priority}")
            sudah_dieksplore.add(sekarang)

            for tetangga, biaya_sisi in graf[sekarang]:
                if tetangga not in sudah_dieksplore:
                    biaya_baru = biaya_sejauh_ini + biaya_sisi
                    prioritas_baru = biaya_baru + heuristik[tetangga]
                    print(
                        f"Menuju dari {sekarang} ke {tetangga} dengan prioritas {prioritas_baru}")
                    perbatasan.append(
                        (prioritas_baru, biaya_baru, tetangga, jalur + [sekarang]))

    return None


start = 'A'
goal = 'J'

path = astar(start, goal, graph, heuristic)
print("Path dari A ke J:", path)
