import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from graph import WeightedDiGraph
from graph import WeightedDiEdge
from queues import IndexMinPQ

class UcsPath:
    def __init__(self,
                 G: WeightedDiGraph,
                 start):
        self.start = start
        self.distTo = {v: 1e300 for v in G.vertexs()}
        self.edge_to = {v: None for v in G.vertexs()}
        self.queue = IndexMinPQ()
        self.search(G, start)

    def search(self,
                G: WeightedDiGraph,
                start):
        '''
        search the graph G from current
        ''' 
        current = start
        self.distTo[current] = 0.0
        self.queue.insert(current, 0.0)
        while not self.queue.is_empty():
            current = self.queue.extract_min()[0]
            for edge in G.adj(current):
                self.relax(edge)

    def relax(self, edge: WeightedDiEdge):
        '''
        relax the edge
        '''
        start = edge.from_vertex()
        end = edge.to_vertex()
        if self.distTo[end] > self.distTo[start] + edge.weight():
            self.distTo[end] = self.distTo[start] + edge.weight()
            self.edge_to[end] = start
            if self.queue.contains(end):
                self.queue.decrease_key(end, self.distTo[end])
            else:
                self.queue.insert(end, self.distTo[end])      

    def has_path_to(self,
                     v) -> bool:
        '''
        return True if there is a path from start to v
        '''
        if v == self.start:
            return True
        if v not in self.distTo:
            return False
        if self.edge_to[v] is None:
            return False
        return True
    
    def path_to(self,
                v)->list:
        '''
        return the path from start to v if there is a path        
        '''
        if not self.has_path_to(v):
            return None
        path = []
        while v != self.start:
            path.append(v)
            v = self.edge_to[v]
        path.append(self.start)
        path.reverse()
        return path
    
if __name__ == '__main__':
    g = WeightedDiGraph()
    g.add_edge('start', 'd', 3)
    g.add_edge('start', 'e', 9)
    g.add_edge('start', 'p', 1)
    g.add_edge('d', 'b', 1)
    g.add_edge('d', 'c', 8)
    g.add_edge('d', 'e', 2)
    g.add_edge('p', 'q', 15)
    g.add_edge('b', 'a', 2)
    g.add_edge('c', 'a', 2)
    g.add_edge('e', 'h', 1)
    g.add_edge('e', 'r', 9)
    g.add_edge('h', 'p', 4)
    g.add_edge('h', 'q', 4)
    g.add_edge('r', 'f', 5)
    g.add_edge('f', 'c', 5)
    g.add_edge('f', 'goal', 5)
    path = UcsPath(g, 'start')
    print(path.path_to('goal'))
    print(path.path_to('a'))
    print(path.path_to('q'))
    print(path.path_to('c'))
    print(path.path_to('h'))
    print(path.path_to('p'))
    print(path.path_to('r'))
    print(path.path_to('f'))
    print(path.path_to('d'))
    print(path.path_to('e'))
    print(path.path_to('start'))
    print(path.path_to('z'))