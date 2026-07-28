import os
import networkx as nx
import matplotlib.pyplot as plt
import random
from algorithms import calculate_average_path_length

def get_network_analysis(graph_manager_obj):
    G = nx.Graph()
    for node, neighbors in graph_manager_obj.graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    return nx.degree_centrality(G)

def save_graph_image(graph_manager_obj, filename="benchmarks/network_plot.png"):
    G = nx.Graph()
    for node, neighbors in graph_manager_obj.graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)
    degrees = dict(G.degree())
    nx.draw_networkx_nodes(G, pos, node_size=[v * 15 for v in degrees.values()], node_color='skyblue')
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    plt.savefig(filename, dpi=150)
    plt.close()

def plot_degree_distribution(graph_manager_obj, filename="benchmarks/degree_distribution.png"):
    degrees = [len(neighbors) for neighbors in graph_manager_obj.graph.values()]
    plt.figure(figsize=(8, 5))
    plt.hist(degrees, bins=20, color='teal')
    plt.savefig(filename)
    plt.close()

def analyze_small_world(graph_manager_obj):
    G = nx.Graph()
    for node, neighbors in graph_manager_obj.graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    avg_clustering = nx.average_clustering(G)
    n = G.number_of_nodes()
    p = (2 * G.number_of_edges()) / (n * (n - 1)) if n > 1 else 0
    random_graph = nx.fast_gnp_random_graph(n, p)
    c_random = nx.average_clustering(random_graph)
    return avg_clustering, c_random

def detect_communities(graph_manager_obj, filename="benchmarks/communities.png"):
    G = nx.Graph()
    for node, neighbors in graph_manager_obj.graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    communities = list(nx.community.greedy_modularity_communities(G))
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, node_size=30, node_color='lightgreen')
    plt.savefig(filename, dpi=150)
    plt.close()
    return len(communities)

def predict_future_links(graph_manager_obj):
    G = nx.Graph()
    for node, neighbors in graph_manager_obj.graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    non_edges = list(nx.non_edges(G))
    if not non_edges: return []
    sampled = random.sample(non_edges, min(len(non_edges), 500))
    preds = list(nx.jaccard_coefficient(G, sampled))
    return sorted(preds, key=lambda x: x[2], reverse=True)[:5]