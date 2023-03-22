maps = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B', 'I', 'H', 'D'],
    'D': ['C', 'H', 'F', 'E'],
    'E': ['D'],
    'F': ['D', 'G'],
    'G':  ['H', 'F'],
    'H': ['C', 'L', 'G', 'D'],
    'I': ['C', 'J', 'K'],
    'J': ['I'],
    'K': ['I', 'L'],
    'L': ['K', 'H']
}


def dfs(peta, mulai):
    # Fungsi ini digunakan untuk mencari jalur menggunakan algoritma DFS (Depth First Search)
    resultNode = []
    tumpukan = [mulai]
    while tumpukan:
        prosesNode = tumpukan.pop()
        # Menambahkan node yang sedang diproses ke dalam hasil
        resultNode.append(prosesNode)
        for anak in peta[prosesNode]:
            if anak not in resultNode:
                # Menambahkan node anak ke tumpukan
                tumpukan.append(anak)
    return resultNode


def dfs_goal(peta, mulai, goal):
    # Fungsi ini digunakan untuk mencari jalur ke node tujuan menggunakan algoritma DFS
    resultNode = []
    jalurNode = {}
    tumpukan = [mulai]
    while tumpukan:
        prosesNode = tumpukan.pop()  # Mengambil node terakhir dari tumpukan
        # Menambahkan node yang sedang diproses ke dalam hasil
        resultNode.append(prosesNode)
        for anak in peta[prosesNode]:
            if anak not in resultNode:
                # Menambahkan node anak ke tumpukan
                tumpukan.append(anak)
                # Menyimpan jalur dari node sebelumnya ke node anak
                jalurNode[anak] = prosesNode
    return jalurNode


def dfs_jalur(jalurnode, mulai, tujuan):
    # Fungsi untuk mengembalikan jalur dari node awal ke node tujuan
    jalur = [tujuan]
    prosesNode = tujuan
    while prosesNode != mulai:
        # Mengatur node yang sedang diproses ke node sebelumnya
        prosesNode = jalurnode[prosesNode]
        # Menambahkan node yang sedang diproses ke jalur
        jalur.append(prosesNode)
    return jalur


print(dfs(maps, 'A'))
jalur = dfs_goal(maps, 'C', 'L')
print(jalur)
solusi = dfs_jalur(jalur, 'C', 'L')
print(solusi[::-1])
