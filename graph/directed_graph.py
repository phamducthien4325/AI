class DirectedGraph:
    def __init__(self):
        self.adjs = {}
   
    def add_edge(self,
                start,
                end):
        if start not in self.adjs:
            self.adjs[start] = []
        if end not in self.adjs:
            self.adjs[end] = []
        self.adjs[start].append(end)

    def adj(self,
            v) -> list:
        '''
        return all vertexs that are adjacent to v
        '''
        return self.adjs[v]
    
    def vertexs(self) -> list:
        '''
        return all vertexs in the graph
        '''
        return list(self.adjs.keys())
