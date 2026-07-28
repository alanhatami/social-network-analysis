import networkx as nx
import matplotlib.pyplot as plt

def get_network_analysis(graph_manager_obj):
    G = nx.Graph()
    for node, neighbors in graph_manager_obj.graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    
    centrality = nx.degree_centrality(G)
    return centrality

def save_graph_image(graph_manager_obj, filename="benchmarks/network_plot.png"):
    G = nx.Graph()
    for node, neighbors in graph_manager_obj.graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
            
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_color='lightgreen', edge_color='gray')
    plt.savefig(filename)
    plt.close()
    print(f"--- Visualization saved to {filename} ---")
