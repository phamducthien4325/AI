import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from graph import DirectedGraph
import unittest

class DirectedGraphTest(unittest.TestCase):
    def test_adj(self):
        g = DirectedGraph()
        g.add_edge('start', 'd')
        g.add_edge('start', 'e')
        g.add_edge('start', 'p')
        g.add_edge('d', 'b')
        g.add_edge('d', 'c')
        g.add_edge('d', 'e')
        g.add_edge('p', 'q')
        g.add_edge('b', 'a')
        g.add_edge('c', 'a')
        g.add_edge('e', 'h')
        g.add_edge('e', 'r')
        g.add_edge('h', 'p')
        g.add_edge('h', 'q')
        g.add_edge('r', 'f')
        g.add_edge('f', 'c')
        g.add_edge('f', 'goal')
        self.assertEqual(g.adj('start'), ['d', 'e', 'p'])
        self.assertEqual(g.adj('d'), ['b', 'c', 'e'])
        self.assertEqual(g.adj('p'), ['q'])
        self.assertEqual(g.adj('b'), ['a'])
        self.assertEqual(g.adj('c'), ['a'])
        self.assertEqual(g.adj('a'), [])
        self.assertEqual(g.adj('e'), ['h', 'r'])
        self.assertEqual(g.adj('q'), [])
        self.assertEqual(g.adj('h'), ['p', 'q'])
        self.assertEqual(g.adj('r'), ['f'])
        self.assertEqual(g.adj('f'), ['c', 'goal'])
        self.assertEqual(g.adj('goal'), [])

    def test_vertexs(self):
        g = DirectedGraph()
        g.add_edge('start', 'd')
        g.add_edge('start', 'e')
        g.add_edge('start', 'p')
        g.add_edge('d', 'b')
        g.add_edge('d', 'c')
        g.add_edge('d', 'e')
        g.add_edge('p', 'q')
        g.add_edge('b', 'a')
        g.add_edge('c', 'a')
        g.add_edge('e', 'h')
        g.add_edge('e', 'r')
        g.add_edge('h', 'p')
        g.add_edge('h', 'q')
        g.add_edge('r', 'f')
        g.add_edge('f', 'c')
        g.add_edge('f', 'goal')
        self.assertEqual(g.vertexs(), ['start', 'd', 'e', 'p', 'b', 'c', 'q', 'a', 'h', 'r', 'f', 'goal'])

    

if __name__ == '__main__':
    unittest.main()