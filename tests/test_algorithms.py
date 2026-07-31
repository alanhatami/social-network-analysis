import pytest
from collections import deque
import math

try:
    from algorithms import bfs_traversal, bfs_shortest_path, dfs_traversal, dijkstra_shortest_path
except ImportError:
    pytest.fail("Could not import functions from algorithms.py. Ensure it's in the Python path.")

from conftest import MockSocialGraph, small_graph, disconnected_graph, weighted_graph, single_node_graph, empty_graph

def test_bfs_traversal_simple(small_graph):
    visited_order = bfs_traversal(small_graph, 0)
    assert visited_order == [0, 1, 2, 3, 4] or visited_order == [0, 2, 1, 3, 4]

def test_bfs_traversal_disconnected(disconnected_graph):
    visited_order = bfs_traversal(disconnected_graph, 0)
    assert visited_order == [0, 1, 2] 
    visited_order_other_comp = bfs_traversal(disconnected_graph, 3)
    assert visited_order_other_comp == [3, 4]

def test_bfs_traversal_empty(empty_graph):
    assert bfs_traversal(empty_graph, 0) == [] 

def test_bfs_traversal_single_node(single_node_graph):
    assert bfs_traversal(single_node_graph, 0) == [0]

def test_bfs_shortest_path_exists(small_graph):
    path = bfs_shortest_path(small_graph, 0, 4)
    assert path == [0, 1, 3, 4] or path == [0, 2, 3, 4]

def test_bfs_shortest_path_no_path(disconnected_graph):
    assert bfs_shortest_path(disconnected_graph, 0, 4) is None

def test_bfs_shortest_path_start_equals_target(small_graph):
    assert bfs_shortest_path(small_graph, 0, 0) == [0]

def test_bfs_shortest_path_empty_graph(empty_graph):
    assert bfs_shortest_path(empty_graph, 0, 1) is None

def test_bfs_shortest_path_single_node_target_not_found(single_node_graph):
     assert bfs_shortest_path(single_node_graph, 0, 1) is None

def test_dfs_traversal_simple(small_graph):
    visited_order = dfs_traversal(small_graph, 0)
    assert visited_order == [0, 2, 3, 1, 4] or visited_order == [0, 1, 3, 2, 4]

def test_dfs_traversal_disconnected(disconnected_graph):
    visited_order = dfs_traversal(disconnected_graph, 0)
    assert visited_order == [0, 1, 2] or visited_order == [0, 2, 1]
    visited_order_other_comp = dfs_traversal(disconnected_graph, 3)
    assert visited_order_other_comp == [3, 4]

def test_dfs_traversal_empty(empty_graph):
    assert dfs_traversal(empty_graph, 0) == []

def test_dfs_traversal_single_node(single_node_graph):
    assert dfs_traversal(single_node_graph, 0) == [0]

def test_dijkstra_shortest_path_exists(weighted_graph):
    path = dijkstra_shortest_path(weighted_graph, 0, 4)
    assert path == [0, 1, 3, 4] or path == [0, 2, 3, 4]

def test_dijkstra_shortest_path_no_path(disconnected_graph):
    assert dijkstra_shortest_path(disconnected_graph, 0, 4) is None

def test_dijkstra_shortest_path_start_equals_target(weighted_graph):
    assert dijkstra_shortest_path(weighted_graph, 0, 0) == [0]

def test_dijkstra_shortest_path_non_existent_nodes(small_graph):
    assert dijkstra_shortest_path(small_graph, 0, 10) is None
    assert dijkstra_shortest_path(small_graph, 10, 0) is None

def test_dijkstra_shortest_path_empty_graph(empty_graph):
    assert dijkstra_shortest_path(empty_graph, 0, 1) is None

def test_dijkstra_shortest_path_single_node(single_node_graph):
    assert dijkstra_shortest_path(single_node_graph, 0, 0) == [0]
    assert dijkstra_shortest_path(single_node_graph, 0, 1) is None
