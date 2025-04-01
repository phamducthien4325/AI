import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
import unittest
from uninform_search import Bfs_path
from graph import DirectedGraph

class Bfs_test(unittest.TestCase):
    def test_path_to(self):
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
        path = Bfs_path(g, 'start')
        self.assertEqual(path.path_to('goal'), ['start', 'e', 'r', 'f', 'goal'])
        self.assertEqual(path.path_to('a'), ['start', 'd', 'b', 'a'])
        self.assertEqual(path.path_to('q'), ['start', 'p', 'q'])
        self.assertEqual(path.path_to('c'), ['start', 'd', 'c'])
        self.assertEqual(path.path_to('h'), ['start', 'e', 'h'])
        self.assertEqual(path.path_to('p'), ['start', 'p'])
        self.assertEqual(path.path_to('r'), ['start', 'e', 'r'])
        self.assertEqual(path.path_to('f'), ['start', 'e', 'r', 'f'])
        self.assertEqual(path.path_to('d'), ['start', 'd'])
        self.assertEqual(path.path_to('e'), ['start', 'e'])
        self.assertEqual(path.path_to('start'), ['start'])
        self.assertEqual(path.path_to('z'), None)

if __name__ == '__main__':
    unittest.main()