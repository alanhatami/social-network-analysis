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