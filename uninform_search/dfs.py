import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from graph import DirectedGraph

class Dfs_path:
    def __init__(self,
                 G: DirectedGraph,
                 start):
        self.start = start
        self.marked = {v: False for v in G.vertexs()}
        self.edge_to = {v: None for v in G.vertexs()}
        self.search(G, start)

    def search(self,
                G: DirectedGraph,
                current):
        '''
        search the graph G from current
        '''
        self.marked[current] = True
        for next_vertical in G.adj(current):
            if not self.marked[next_vertical]:
                self.edge_to[next_vertical] = current
                self.search(G, next_vertical)

    def has_path_to(self,
                     v):
        '''
        return True if there is a path from start to v
        '''
        if v not in self.marked.keys():
            return False
        return self.marked[v]
    
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