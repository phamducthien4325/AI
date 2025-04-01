import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
import unittest
from uninform_search import UcsPath
from graph import WeightedDiGraph

class Ucs_test(unittest.TestCase):
    def test_path_to(self):
        g = WeightedDiGraph()
        g.add_edge('start', 'd', 3)
        g.add_edge('start', 'e', 9)
        g.add_edge('start', 'p', 1)
        g.add_edge('d', 'b', 1)
        g.add_edge('d', 'c', 8)
        g.add_edge('d', 'e', 2)
        g.add_edge('p', 'q', 15)
        g.add_edge('q', 'r', 3)
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
        self.assertEqual(path.path_to('goal'), ['start', 'd', 'e', 'h', 'q', 'r', 'f', 'goal'])
        self.assertEqual(path.path_to('a'), ['start', 'd', 'b', 'a'])
        self.assertEqual(path.path_to('q'), ['start', 'd', 'e', 'h', 'q'])
        self.assertEqual(path.path_to('c'), ['start', 'd', 'c'])
        self.assertEqual(path.path_to('h'), ['start', 'd', 'e', 'h'])
        self.assertEqual(path.path_to('p'), ['start', 'p'])
        self.assertEqual(path.path_to('r'), ['start', 'd', 'e', 'h', 'q', 'r'])
        self.assertEqual(path.path_to('f'), ['start', 'd', 'e', 'h', 'q', 'r', 'f'])
        self.assertEqual(path.path_to('d'), ['start', 'd'])
        self.assertEqual(path.path_to('e'), ['start', 'd', 'e'])
        self.assertEqual(path.path_to('start'), ['start'])
        self.assertEqual(path.path_to('z'), None)

if __name__ == '__main__':
    unittest.main()