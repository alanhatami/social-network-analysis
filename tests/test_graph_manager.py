import pytest
from collections import defaultdict

try:
    from conftest import MockSocialGraph
except ImportError:
    class MockSocialGraph:
        def __init__(self):
            self.graph = defaultdict(list)
            self.nodes = set()
            self.edges = []

        def add_node(self, node):
            if node not in self.nodes:
                self.nodes.add(node)
                if node not in self.graph:
                    self.graph[node] = []

        def add_edge(self, u, v):
            self.add_node(u)
            self.add_node(v)
            if v not in self.graph[u]:
                self.graph[u].append(v)
            if u not in self.graph[v]:
                self.graph[v].append(u)
            if (u, v) not in self.edges and (v, u) not in self.edges:
                self.edges.append((u, v))

        def load_from_csv(self, file_path):
            pass 

@pytest.fixture
def sample_graph_manager():
    graph_manager = MockSocialGraph()
    graph_manager.add_edge(0, 1)
    graph_manager.add_edge(0, 2)
    graph_manager.add_edge(1, 3)
    graph_manager.add_edge(2, 3)
    return graph_manager

def test_add_node(sample_graph_manager):
    initial_nodes = len(sample_graph_manager.nodes)
    sample_graph_manager.add_node(5)
    assert 5 in sample_graph_manager.nodes
    assert len(sample_graph_manager.nodes) == initial_nodes + 1
    assert 5 in sample_graph_manager.graph 

def test_add_existing_node(sample_graph_manager):
    initial_nodes = len(sample_graph_manager.nodes)
    sample_graph_manager.add_node(0) 
    assert 0 in sample_graph_manager.nodes
    assert len(sample_graph_manager.nodes) == initial_nodes 

def test_add_edge(sample_graph_manager):
    initial_edges = len(sample_graph_manager.edges)
    sample_graph_manager.add_edge(1, 2) 
    assert 2 in sample_graph_manager.graph[1]
    assert 1 in sample_graph_manager.graph[2]
    assert len(sample_graph_manager.edges) == initial_edges + 1 

def test_add_edge_new_nodes(sample_graph_manager):
    initial_nodes = len(sample_graph_manager.nodes)
    initial_edges = len(sample_graph_manager.edges)
    sample_graph_manager.add_edge(5, 6) 
    assert 5 in sample_graph_manager.nodes
    assert 6 in sample_graph_manager.nodes
    assert len(sample_graph_manager.nodes) == initial_nodes + 2
    assert len(sample_graph_manager.edges) == initial_edges + 1
    assert 6 in sample_graph_manager.graph[5]

def test_add_duplicate_edge(sample_graph_manager):
    initial_edges = len(sample_graph_manager.edges)
    sample_graph_manager.add_edge(0, 1) 
    assert len(sample_graph_manager.edges) == initial_edges 
    assert sample_graph_manager.graph[0].count(1) == 1 

def test_graph_properties(sample_graph_manager):
    assert len(sample_graph_manager.nodes) == 5 
    assert len(sample_graph_manager.edges) == 4 
    assert sample_graph_manager.graph[0] == [1, 2]
    assert sample_graph_manager.graph[3] == [1, 2, 4]

def test_empty_graph_operations(empty_graph):
    assert len(empty_graph.nodes) == 0
    assert len(empty_graph.edges) == 0
    empty_graph.add_node(10)
    assert 10 in empty_graph.nodes
    assert len(empty_graph.nodes) == 1
    assert empty_graph.graph[10] == []
    empty_graph.add_edge(10, 11)
    assert 11 in empty_graph.nodes
    assert 11 in empty_graph.graph[10]
    assert len(empty_graph.edges) == 1
