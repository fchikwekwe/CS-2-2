
from challenge_1 import Graph
import unittest

class GraphTest(unittest.TestCase):

    def test_init(self):
        nothing = Graph('empty.txt')
        assert nothing.file == 'empty.txt'
    
    def test_empty_graph(self):
        nothing = Graph('empty.txt')
        assert nothing.vertex_count() == 0
        assert nothing.edge_count() == 0 
        assert nothing.edge_list() == []

    def test_vertex_count(self):
        g = Graph('sample_graph_1.txt')
        assert g.vertex_count() == 4
        assert g.vertex_count() != 0 
        
        other_g = Graph('sample_graph_2.txt')
        assert other_g.vertex_count() == 10
        assert other_g.vertex_count() != 0 

        another_g = Graph('sample_graph_3.txt')
        assert another_g.vertex_count() == 10
        assert another_g.vertex_count() != 0

    def test_edge_count(self):
        g = Graph('sample_graph_1.txt')
        assert g.edge_count() == 4
        assert g.edge_count() != 0 
        
        other_g = Graph('sample_graph_2.txt')
        assert other_g.edge_count() == 12
        assert other_g.edge_count() != 0 

        another_g = Graph('sample_graph_3.txt')
        assert another_g.edge_count() == 27
        # make sure its not including empty parentheses or invalid data
        assert another_g.edge_count() != 29 
        assert another_g.edge_count() != 31
        assert another_g.edge_count() != 0
    
    def test_edge_list(self):
        pass
