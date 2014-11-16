LARGE_DISTANCE = 1000000

class Graph(object):
    """docstring for Graph"""
    def __init__(self):
        super(Graph, self).__init__()
        self.graph = {}
        self.N = 0
        self.M = 0

    def load(self, filename):
        for l in open(filename):
            tokens = l.strip().replace('\t', ' ').split(' ')
            edges = tokens[1:]
            v = int(tokens[0])
            self.graph[v] = []
            for edge in edges:
                tmp = [int(x) for x in edge.split(',')]
                self.graph[v].append((tmp[0], tmp[1]))
            self.M += len(edges)
        self.N = len(self.graph)

    def shortestPath(self, s, t):
        '''
        find the shortest distance (path) from s to t
        '''
        nodesProcessed = [s]
        shortestDistances = [0] * (self.N + 1)  # node index start at 1
        shortestPath = [[]] * (self.N + 1)
        
        while len(nodesProcessed) < self.N:
            minNewDistance = LARGE_DISTANCE
            for v in nodesProcessed:
                for w, dist in self.graph[v]:
                    if w not in nodesProcessed:
                        newDist = shortestDistances[v] + dist
                        if newDist < minNewDistance:
                            minNewDistance = newDist
                            newV = v
                            newW = w
            # print('adding new node {0} from {1}'.format(newW, newV))
            nodesProcessed.append(newW)
            shortestDistances[newW] = minNewDistance
            shortestPath[newW] = shortestPath[newV] + [newW]
            if newW == t:
                return shortestDistances[t], shortestPath[t]
        return LARGE_DISTANCE


    def __str__(self):
        s = '{0} nodes \n{1} edges\n'.format(self.N, self.M)
        s += '\n'.join(['[{0}]: {1}'.format(k, v) for k, v in self.graph.items()])
        return s

def main():
    filename = 'dijkstraData.txt'
    # filename = 'testcase_4'
    g = Graph()
    g.load(filename)
    print(g)

    endingList = [7,37,59,82,99,115,133,165,188,197]
    start = 1
    results = []
    for t in endingList:
        print('-'*30)
        if t == start:
            dist = 0
            path = [t]
        else:
            dist, path = g.shortestPath(start, t)
        results.append(dist)
        print(t, dist, path)
    
    print('-'*30)
    print(','.join([str(d) for d in results]))  # home work format


if __name__ == '__main__':
    main()