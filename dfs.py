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
    resultNode = []
    tumpukan = [mulai]
    while tumpukan:
        prosesNode = tumpukan.pop()
        resultNode.append(prosesNode)
        for anak in peta[prosesNode]:
            if anak not in resultNode:
                tumpukan.append(anak)
    return resultNode


def dfs_goal(peta, mulai, goal):
    resultNode = []
    jalurNode = {}
    tumpukan = [mulai]
    while tumpukan:
        prosesNode = tumpukan.pop()
        resultNode.append(prosesNode)
        for anak in peta[prosesNode]:
            if anak not in resultNode:
                tumpukan.append(anak)
                jalurNode[anak] = prosesNode
    return jalurNode


def dfs_jalur(jalurnode, mulai, tujuan):
    jalur = [tujuan]
    prosesNode = tujuan
    while prosesNode != mulai:
        prosesNode = jalurnode[prosesNode]
        jalur.append(prosesNode)
    return jalur


print(dfs(maps, 'A'))
jalur = dfs_goal(maps, 'C', 'L')
print(jalur)
solusi = dfs_jalur(jalur, 'C', 'L')
print(solusi[::-1])
