class WeightedDiEdge:
    def __init__(self, v, w, weight: float):
        self.v = v
        self.w = w
        self._weight: float = weight

    def from_vertex(self):
        return self.v

    def to_vertex(self):
        return self.w
    
    def weight(self) -> float:
        return self._weight