import os
from graph_manager import SocialGraph
from algorithms import bfs_shortest_path, dfs_traversal
from analyzer import (get_network_analysis, save_graph_image, plot_degree_distribution, 
                      analyze_small_world, detect_communities, predict_future_links)

def main():
    os.makedirs("benchmarks", exist_ok=True)
    sg = SocialGraph()
    if not sg.load_from_csv("data/social_network.csv"):
        print("Error: CSV not found in data/")
        return
    
    nodes = sorted(list(sg.nodes))
    if len(nodes) < 2: return

    print("Running Analytics...")
    save_graph_image(sg)
    plot_degree_distribution(sg)
    detect_communities(sg)