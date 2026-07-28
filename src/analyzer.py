import os
import networkx as nx
import matplotlib.pyplot as plt
import random

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
            
    sampled_nodes = random.sample(list(G.nodes()), min(len(G.nodes()), 300))
    sub_G = G.subgraph(sampled_nodes)
    
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(sub_G, seed=42)
    degrees = dict(sub_G.degree())
    nx.draw_networkx_nodes(sub_G, pos, node_size=[v * 15 for v in degrees.values()], node_color='skyblue')
    nx.draw_networkx_edges(sub_G, pos, alpha=0.2)
    plt.title("Social Network Subgraph (Sampled Nodes)")
    plt.savefig(filename, dpi=150)
    plt.close()

def plot_degree_distribution(graph_manager_obj, filename="benchmarks/degree_distribution.png"):
    degrees = [len(neighbors) for neighbors in graph_manager_obj.graph.values()]
    plt.figure(figsize=(8, 5))
    plt.hist(degrees, bins=25, color='teal', edgecolor='black', alpha=0.7)
    plt.xlabel('Degree (Number of Friends)')
    plt.ylabel('Count of Users')
    plt.title('Degree Distribution of Social Network')
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
    
    sampled_nodes = random.sample(list(G.nodes()), min(len(G.nodes()), 300))
    sub_G = G.subgraph(sampled_nodes)
    
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(sub_G, seed=42)
    
    color_map = []
    for node in sub_G:
        assigned = False
        for idx, comm in enumerate(communities[:8]):  
            if node in comm:
                color_map.append(idx)
                assigned = True
                break
        if not assigned:
            color_map.append(8)
            
    nx.draw(sub_G, pos, node_size=35, node_color=color_map, cmap=plt.cm.tab10, edge_color='gray', alpha=0.3)
    plt.title("Detected Communities (Sampled visualization)")
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
    sampled = random.sample(non_edges, min(len(non_edges), 1000))
    preds = list(nx.jaccard_coefficient(G, sampled))
    return sorted(preds, key=lambda x: x[2], reverse=True)[:5]
