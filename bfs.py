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


def bfs(peta, mulai):
    resultNode = []
    antrian = [mulai]
    while antrian:
        prosesNode = antrian.pop(0)
        resultNode.append(prosesNode)
        for anak in peta[prosesNode]:
            if anak not in resultNode:
                antrian.append(anak)
    return resultNode


def bfs_goal(peta, mulai, goal):
    resultNode = []
    jalurNode = {}
    antrian = [mulai]
    while antrian:
        prosesNode = antrian.pop(0)
        resultNode.append(prosesNode)
        for anak in peta[prosesNode]:
            if anak not in resultNode:
                antrian.append(anak)
                jalurNode[anak] = prosesNode
    return jalurNode


print(bfs(maps, 'A'))
print(bfs_goal(maps, 'C', 'L'))
