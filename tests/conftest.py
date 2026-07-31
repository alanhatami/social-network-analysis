import pytest
from collections import defaultdict
import math

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
def small_graph():
    graph = MockSocialGraph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    return graph

@pytest.fixture
def weighted_graph():
    graph = MockSocialGraph()
    graph.add_edge(0, 1) 
    graph.add_edge(0, 2) 
    graph.add_edge(1, 3) 
    graph.add_edge(2, 3) 
    graph.add_edge(3, 4) 
    return graph

@pytest.fixture
def disconnected_graph():
    graph = MockSocialGraph()
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(3, 4) 
    return graph

@pytest.fixture
def triangle_graph():
    graph = MockSocialGraph()
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    return graph

@pytest.fixture
def line_graph():
    graph = MockSocialGraph()
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    return graph

@pytest.fixture
def empty_graph():
    return MockSocialGraph()

@pytest.fixture
def single_node_graph():
    graph = MockSocialGraph()
    graph.add_node(0)
    return graph

@pytest.fixture
def complete_graph_small():
    graph = MockSocialGraph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    return graph

try:
    from algorithms import bfs_traversal, bfs_shortest_path, dfs_traversal, dijkstra_shortest_path
    from graph_manager import SocialGraph 
except ImportError:
    print("Warning: Could not import from algorithms.py or graph_manager.py. Ensure they are in the Python path or copied to tests/.")
    pass 

try:
    from analyzer import (
        get_network_analysis, save_graph_image, plot_degree_distribution,
        analyze_small_world, detect_communities, predict_future_links
    )
except ImportError:
    print("Warning: Could not import from analyzer.py. Ensure it is in the Python path or copied to tests/.")
    pass
