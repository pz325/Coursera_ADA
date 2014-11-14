import time

# comment out all log when processing the large dataset
DEBUG = False

def log(message):
    if DEBUG:
        print(message)

N = 900000

class Graph(object):
    """docstring for Graph"""
    def __init__(self):
        super(Graph, self).__init__()
        self.graph = {i:[] for i in range(1, N+1)}
        self.numNodesProcessed = 0
        self.nodesExplored = [False] * N
        self.nodesFinished = [False] * N
        self.finishingTimes = [0] * N
        self.t = 0
        self.sccs = {}  # key is the leader, value is nodes in that SCC
        self.curretnLeader = 0
    
    def load(self, filename):
        maxNode = 0
        self.M = 0
        for l in open(filename):
            self.M += 1
            uv = [int(x) for x in l.split(' ')[0:2]]
            tail, head = uv[0], uv[1]
            if tail > maxNode: maxNode = tail
            if head > maxNode: maxNode = head
            self.graph[tail].append(head)        
        self.N = maxNode

    def reverse(self):
        graphRev = Graph();
        for k, v in self.graph.items():
            for i in v:
                graphRev.graph[i].append(k)
        graphRev.N = self.N
        graphRev.M = self.M
        return graphRev

    def __str__(self):
        s = 'N: {0}\n'.format(self.N)
        s +=  str(self.graph)
        return s

def dfs_recursive(graph, i):
    graph.nodesExplored[i] = True
    graph.sccs[graph.curretnLeader].append(i)
    for j in graph.graph[i]:
        if not graph.nodesExplored[j]:
            dfs_recursive(graph, j)
    graph.t += 1
    graph.finishingTimes[i] = graph.t
    pass


def dfs_iterative(graph, i):
    dfsStack = [i]
    while len(dfsStack) > 0:
        # log('stack length: {0}'.format(len(dfsStack)))
        u = dfsStack.pop()
        # log('    visiting {0}'.format(u))
        if not graph.nodesExplored[u]:
            graph.nodesExplored[u] = True
            dfsStack.append(u)
            dfsStack += [j for j in graph.graph[u] if not graph.nodesExplored[j]]
            # log('stack for next iteration {0}'.format(dfsStack))
        else:
            if not graph.nodesFinished[u]:
                graph.t += 1
                # log('    {0} is visited at {1}'.format(u, graph.t))
                graph.finishingTimes[graph.t] = u
                graph.nodesFinished[u] = True
                graph.sccs[graph.curretnLeader].append(u)
            # log('stack for next iteration {0}'.format(dfsStack))

def dfsLoop(graph, sequence=None):
    if not sequence:
        sequence = range(graph.N, 0, -1)
    for i in sequence:
        # print('loop node {0}'.format(i))
        if not graph.nodesExplored[i]:
            graph.curretnLeader = i
            if graph.curretnLeader not in graph.sccs:
                graph.sccs[graph.curretnLeader] = []
            # log('found a new SCC leaded by {0}'.format(graph.curretnLeader))
            dfs_iterative(graph, i)
            # dfs_recursive(graph, i)

def main():
    # graphFile = 'SCC.txt'
    graphFile = 'scc_40000'
    graph = Graph()
    print('load graph from {0}'.format(graphFile))
    startTime = time.time()
    graph.load(graphFile)
    print('graph has {0} nodes.'.format(graph.N))
    print('graph has {0} edges.'.format(graph.M))
    print("--- Load graph takes {0} seconds ---".format(time.time() - startTime))

    # reverse G
    print('reverse graph')
    startTime = time.time()
    graphRev = graph.reverse()
    print('reversed graph has {0} nodes.'.format(graphRev.N))
    print('reversed graph has {0} edges.'.format(graphRev.M))
    print("--- Reverse graph takes {0} seconds ---".format(time.time() - startTime))
    
    print('DFS-LOOP on G rev')
    startTime = time.time()
    dfsLoop(graphRev)
    # log(graphRev.finishingTimes[0:graphRev.N+1])
    print("--- First DFS-LOOP takes {0} seconds ---".format(time.time() - startTime))

    print('DFS-LOOP on G')
    startTime = time.time()
    seq = graphRev.finishingTimes[1:graphRev.N+1][::-1]
    # log('seq: {0}'.format(seq))
    dfsLoop(graph, seq)
    print("--- Second DFS-LOOP takes {0} seconds ---".format(time.time() - startTime))

    print('found {0} SCCs'.format(len(graph.sccs)))
    sccCount = sorted([len(v) for v in graph.sccs.values()], reverse=True)
    if len(sccCount) < 5:
        sccCount += [0] * (5 - len(sccCount))
    else:
        sccCount = sccCount[0:5]
    print(','.join([str(c) for c in sccCount]))


if __name__ == '__main__':
    main()
