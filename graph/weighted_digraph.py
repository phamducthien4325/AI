from .edges import WeightedDiEdge
from typing import List

class WeightedDiGraph:
    def __init__(self):
        self.adjs = {}
   
    def add_edge(self,
                start,
                end,
                weight: float) -> None:
        if start not in self.adjs:
            self.adjs[start] = []
        if end not in self.adjs:
            self.adjs[end] = []
        v = WeightedDiEdge(start, end, weight)
        self.adjs[start].append(v)

    def adj(self,
            v) -> List[WeightedDiEdge]:
        '''
        return all vertexs that are adjacent to v
        '''
        return self.adjs[v]
    
    def vertexs(self) -> list:
        '''
        return all vertexs in the graph
        '''
        return list(self.adjs.keys())

