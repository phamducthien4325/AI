import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from graph import WeightedDiGraph
from graph import WeightedDiEdge
from queues import IndexMinPQ

class GreedyBestFirstSearch:
    def __init__(self,
                 G: WeightedDiGraph,
                 heuristic,
                 start,
                 end):
        self.start = start
        self.h = heuristic
        self.marked = {v: False for v in G.vertexs()}
        self.edge_to = {v: None for v in G.vertexs()}
        self.queue = IndexMinPQ()
        self.search(G, start, end)

    def search(self,
                G: WeightedDiGraph,
                start,
                end):
        '''
        search the graph G from current
        ''' 
        current = start
        self.marked[current] = True
        self.queue.insert(current, 0.0)
        while not self.queue.is_empty():
            current = self.queue.extract_min()[0]
            for edge in G.adj(current):
                if not self.marked[edge.to_vertex()]:
                    self.queue.insert(edge.to_vertex(), self.h(edge.to_vertex()))
                    self.marked[edge.to_vertex()] = True
                    self.edge_to[edge.to_vertex()] = current
            if current == end:
                break

    def has_path_to(self,
                     v) -> bool:
        '''
        return True if there is a path from start to v
        '''
        if v == self.start:
            return True
        if v not in self.marked:
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