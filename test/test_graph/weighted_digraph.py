import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from graph import WeightedDiGraph
import unittest
from typing import List
from graph import WeightedDiEdge

class WeightedDigraphTest(unittest.TestCase):
    def test_adj(self):
        g = WeightedDiGraph()
        g.add_edge('start', 'd', 3.0)
        g.add_edge('start', 'e', 9.0)
        g.add_edge('start', 'p', 1.0)
        g.add_edge('d', 'b', 1.0)
        g.add_edge('d', 'c', 8.0)
        g.add_edge('d', 'e', 2.0)
        g.add_edge('p', 'q', 15.0)
        g.add_edge('b', 'a', 2.0)
        g.add_edge('c', 'a', 2.0)
        g.add_edge('e', 'h', 1.0)
        g.add_edge('e', 'r', 9.0)
        g.add_edge('h', 'p', 4.0)
        g.add_edge('h', 'q', 4.0)
        g.add_edge('r', 'f', 5.0)
        g.add_edge('f', 'c', 5.0)
        g.add_edge('f', 'goal', 5.0)
        self.assertEqual(read_end_vertex(g.adj('start')), ['d', 'e', 'p'])
        self.assertEqual(read_end_vertex(g.adj('d')), ['b', 'c', 'e'])
        self.assertEqual(read_end_vertex(g.adj('p')), ['q'])
        self.assertEqual(read_end_vertex(g.adj('b')), ['a'])
        self.assertEqual(read_end_vertex(g.adj('c')), ['a'])
        self.assertEqual(read_end_vertex(g.adj('a')), [])
        self.assertEqual(read_end_vertex(g.adj('e')), ['h', 'r'])
        self.assertEqual(read_end_vertex(g.adj('q')), [])
        self.assertEqual(read_end_vertex(g.adj('h')), ['p', 'q'])
        self.assertEqual(read_end_vertex(g.adj('r')), ['f'])
        self.assertEqual(read_end_vertex(g.adj('f')), ['c', 'goal'])
        self.assertEqual(read_end_vertex(g.adj('goal')), [])

    def test_vertexs(self):
        g = WeightedDiGraph()
        g.add_edge('start', 'd', 3.0)
        g.add_edge('start', 'e', 9.0)
        g.add_edge('start', 'p', 1.0)
        g.add_edge('d', 'b', 1.0)
        g.add_edge('d', 'c', 8.0)
        g.add_edge('d', 'e', 2.0)
        g.add_edge('p', 'q', 15.0)
        g.add_edge('b', 'a', 2.0)
        g.add_edge('c', 'a', 2.0)
        g.add_edge('e', 'h', 1.0)
        g.add_edge('e', 'r', 9.0)
        g.add_edge('h', 'p', 4.0)
        g.add_edge('h', 'q', 4.0)
        g.add_edge('r', 'f', 5.0)
        g.add_edge('f', 'c', 5.0)
        g.add_edge('f', 'goal', 5.0)
        self.assertEqual(g.vertexs(), ['start', 'd', 'e', 'p', 'b', 'c', 'q', 'a', 'h', 'r', 'f', 'goal'])

def read_end_vertex(edges: List[WeightedDiEdge]) -> list:
    return [edge.to_vertex() for edge in edges]

if __name__ == '__main__':
    unittest.main()