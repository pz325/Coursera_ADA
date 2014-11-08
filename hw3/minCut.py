import random
from copy import deepcopy

def loadGraph(filename):
    graph = {}
    for l in open(filename).readlines():
        if '\t' in l:
            delimiter = '\t'
        else:
            delimiter = ' '
        vertices = [int(v) for v in l.strip().split(delimiter)]
        graph[vertices[0]] = vertices[1:]
    return graph

def pickEdge(graph):
    u = random.choice(graph.keys())
    v = random.choice(graph[u])
    return (u, v)

def contractVertices(graph, u, v):
    '''
    contract v to u
    remove self-loops
    '''
    graph[u] = [vertex for vertex in graph[u] if vertex != v]
    graph[v] = [vertex for vertex in graph[v] if vertex != u]
    graph[u] += graph[v]
    del graph[v]
    for key, value in graph.items():
        if key == u: continue
        graph[key] = [u if vertex == v else vertex for vertex in graph[key]]
    # print('contract {0} and {1}'.format(u, v))
    # print('after contraction: ', graph)

def randomContractionCut(graph):
    # print(graph)
    randomSeed = random.randrange(99999999)
    random.seed(randomSeed)
    # print(randomSeed)
    while(len(graph) > 2):
        # pick remaining edge
        picked = pickEdge(graph)
        # contract graph
        contractVertices(graph, picked[0], picked[1])
    return len(graph.values()[0])


def minCut(graph):
    N = len(graph) ** 2;
    m = len(graph)
    for x in range(0, N):
        tmp = randomContractionCut(deepcopy(graph))
        print('iteration:', x, 'cut', tmp, 'minCut', m)
        if tmp < m:
            m = tmp
    return m

def testMinCut(graph):
    x = 0
    m = 0
    while m != 2:
        m = randomContractionCut(deepcopy(graph))
        x += 1
    print(x)


def main():
    filename = 'kargerMinCut.txt'
    # filename = '12nodes_3.txt'
    graph = loadGraph(filename)
    print('V', len(graph))

    m = minCut(graph)
    print(m)
    # testMinCut(graph)

if __name__ == '__main__':
    main()