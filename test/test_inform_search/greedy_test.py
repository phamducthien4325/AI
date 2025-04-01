import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

import unittest
from inform_search import GreedyBestFirstSearch
from graph import WeightedDiGraph

class GreedyTest(unittest.TestCase):
    def test_path_to(self):
        g = WeightedDiGraph()
        g.add_edge('A', 'Z', 75)
        g.add_edge('A', 'S', 140)
        g.add_edge('A', 'T', 118)
        g.add_edge('Z', 'O', 71)
        g.add_edge('O', 'S', 151)
        g.add_edge('T', 'L', 111)
        g.add_edge('L', 'M', 70)
        g.add_edge('M', 'D', 75)
        g.add_edge('D', 'C', 120)
        g.add_edge('S', 'F', 99)
        g.add_edge('S', 'R', 80)
        g.add_edge('R', 'P', 97)
        g.add_edge('R', 'C', 146)
        g.add_edge('C', 'P', 138)
        g.add_edge('P', 'B', 101)
        g.add_edge('F', 'B', 211)
        g.add_edge('B', 'G', 90)
        g.add_edge('B', 'U', 85)
        g.add_edge('U', 'H', 98)
        g.add_edge('U', 'V', 142)
        g.add_edge('H', 'E', 86)
        g.add_edge('V', 'I', 92)
        g.add_edge('I', 'N', 87)
        path = GreedyBestFirstSearch(g, self.heuristic, 'A', 'B')
        self.assertEqual(path.path_to('B'), ['A', 'S', 'F', 'B'])

    _h = {
        'A': 366,  # Arad
        'B': 0,    # Bucharest
        'C': 160,  # Craiova
        'D': 242,  # Dobreta
        'E': 161,  # Eforie
        'F': 178,  # Fagaras
        'G': 77,   # Giurgiu
        'H': 151,  # Hirsova
        'I': 226,  # Iasi
        'L': 244,  # Lugoj
        'M': 241,  # Mehadia
        'N': 234,  # Neamt
        'O': 380,  # Oradea
        'P': 98,   # Pitesti
        'R': 193,  # Rimnicu Vilcea
        'S': 253,  # Sibiu
        'T': 329,  # Timisoara
        'U': 80,   # Urziceni
        'V': 199,  # Vaslui
        'Z': 374   # Zerind
    }

    def heuristic(self, v):
        return self._h[v]


if __name__ == '__main__':
    unittest.main()