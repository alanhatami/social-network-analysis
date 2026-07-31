import pytest
import os
import networkx as nx
import matplotlib.pyplot as plt 
from unittest.mock import patch 

try:
    from analyzer import (
        get_network_analysis, save_graph_image, plot_degree_distribution,
        analyze_small_world, detect_communities, predict_future_links
    )
except ImportError:
    pytest.fail("Could not import functions from analyzer.py. Ensure it's in the Python path.")

from conftest import MockSocialGraph, small_graph, weighted_graph, disconnected_graph, triangle_graph, line_graph, empty_graph, single_node_graph, complete_graph_small

BENCHMARKS_DIR = "benchmarks"
TEST_FILES = [
    "network_plot.png",
    "degree_distribution.png",
    "communities.png"
]

@pytest.fixture(autouse=True)
def setup_benchmarks_dir():
    if not os.path.exists(BENCHMARKS_DIR):
        os.makedirs(BENCHMARKS_DIR)
    for file_name in TEST_FILES:
        file_path = os.path.join(BENCHMARKS_DIR, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
    yield

def test_get_network_analysis(small_graph):
    expected_centrality = {0: 0.5, 1: 0.5, 2: 0.5, 3: 0.75, 4: 0.25}
    centrality = get_network_analysis(small_graph)
    for node, value in expected_centrality.items():
        assert node in centrality
        assert abs(centrality[node] - value) < 1e-6

def test_get_network_analysis_empty(empty_graph):
    assert get_network_analysis(empty_graph) == {}

def test_save_graph_image(small_graph):
    filename = os.path.join(BENCHMARKS_DIR, "network_plot.png")
    save_graph_image(small_graph, filename)
    assert os.path.exists(filename)
    try:
        img = plt.imread(filename)
        assert img.shape[0] > 0 and img.shape[1] > 0 
    except Exception as e:
        pytest.fail(f"Could not read generated image: {e}")

@pytest.mark.skip(reason="Skipping image generation tests due to potential for false positives/negatives and performance impact.")
def test_save_graph_image_no_plot(small_graph):
    pass

def test_plot_degree_distribution(small_graph):
    filename = os.path.join(BENCHMARKS_DIR, "degree_distribution.png")
    plot_degree_distribution(small_graph, filename)
    assert os.path.exists(filename)
    try:
        img = plt.imread(filename)
        assert img.shape[0] > 0 and img.shape[1] > 0
    except Exception as e:
        pytest.fail(f"Could not read generated image: {e}")

def test_plot_degree_distribution_empty(empty_graph):
    filename = os.path.join(BENCHMARKS_DIR, "degree_distribution_empty.png")
    plot_degree_distribution(empty_graph, filename)
    assert os.path.exists(filename)
    try:
        img = plt.imread(filename)
        assert img.shape[0] > 0 and img.shape[1] > 0
    except Exception as e:
        pytest.fail(f"Could not read generated image for empty graph: {e}")

def test_analyze_small_world_triangle(triangle_graph):
    avg_c, rand_c = analyze_small_world(triangle_graph)
    assert abs(avg_c - 1.0) < 1e-6
    assert 0.9 <= rand_c <= 1.0

def test_analyze_small_world_line(line_graph):
    avg_c, rand_c = analyze_small_world(line_graph)
    assert abs(avg_c - 0.0) < 1e-6
    assert 0.0 <= rand_c < 1.0 

def test_analyze_small_world_empty(empty_graph):
    avg_c, rand_c = analyze_small_world(empty_graph)
    assert math.isinf(avg_c) or math.isnan(avg_c) 
    assert math.isinf(rand_c) or math.isnan(rand_c)

def test_analyze_small_world_single_node(single_node_graph):
    avg_c, rand_c = analyze_small_world(single_node_graph)
    assert math.isinf(avg_c) or math.isnan(avg_c) 
    assert math.isinf(rand_c) or math.isnan(rand_c)

def test_detect_communities_basic(small_graph):
    filename = os.path.join(BENCHMARKS_DIR, "communities.png")
    num_communities = detect_communities(small_graph, filename)
    assert os.path.exists(filename)
    assert num_communities > 0 

def test_detect_communities_disconnected(disconnected_graph):
    filename = os.path.join(BENCHMARKS_DIR, "communities_disconnected.png")
    num_communities = detect_communities(disconnected_graph, filename)
    assert os.path.exists(filename)
    assert num_communities == 2 

def test_detect_communities_complete(complete_graph_small):
    filename = os.path.join(BENCHMARKS_DIR, "communities_complete.png")
    num_communities = detect_communities(complete_graph_small, filename)
    assert os.path.exists(filename)
    assert num_communities == 1 

def test_detect_communities_empty(empty_graph):
    filename = os.path.join(BENCHMARKS_DIR, "communities_empty.png")
    num_communities = detect_communities(empty_graph, filename)
    assert os.path.exists(filename)
    assert num_communities == 0 

def test_predict_future_links_no_non_edges(complete_graph_small):
    predictions = predict_future_links(complete_graph_small)
    assert predictions == []

def test_predict_future_links_some_edges(small_graph):
    predictions = predict_future_links(small_graph)
    assert len(predictions) > 0 
    for u, v, score in predictions:
        assert isinstance(u, int)
        assert isinstance(v, int)
        assert isinstance(score, float)
        assert score >= 0.0 and score <= 1.0 

def test_predict_future_links_disconnected(disconnected_graph):
    predictions = predict_future_links(disconnected_graph)
    assert len(predictions) == 0 
    assert len(predictions) >= 0 

def test_predict_future_links_empty(empty_graph):
    assert predict_future_links(empty_graph) == []
