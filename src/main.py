import os
from graph_manager import SocialGraph
from algorithms import bfs_shortest_path, dijkstra_shortest_path, dfs_traversal
from analyzer import (get_network_analysis, save_graph_image, plot_degree_distribution, 
                      analyze_small_world, detect_communities, predict_future_links)

def main():
    # ساخت پوشه خروجی‌ها در صورت عدم وجود
    os.makedirs("benchmarks", exist_ok=True)
    
    sg = SocialGraph()
    print("Loading dataset...")
    if not sg.load_from_csv("data/social_network.csv"):
        print("Error: CSV not found in data/social_network.csv. Make sure you run from the project root directory.")
        return
    
    nodes = sorted(list(sg.nodes))
    print(f"Dataset Loaded Successfully! Nodes: {len(nodes)}, Edges: {sum(len(neighbors) for neighbors in sg.graph.values()) // 2}")

    print("\n--- Running Graph Traversals & Path Findings (Demo) ---")
    if len(nodes) >= 2:
        # انتخاب دو گره تصادفی برای نمایش کارکرد الگوریتم‌ها
        start_node = 0
        target_node = 100
        print(f"Executing BFS Shortest Path from Node {start_node} to {target_node}...")
        path_bfs = bfs_shortest_path(sg, start_node, target_node)
        print(f"BFS Path: {path_bfs}")
        
        print(f"\nExecuting Dijkstra Shortest Path from Node {start_node} to {target_node}...")
        path_dijkstra = dijkstra_shortest_path(sg, start_node, target_node)
        print(f"Dijkstra Path: {path_dijkstra}")
    
    print("\n--- Running Advanced Analytics & Plotting ---")
    print("1. Plotting degree distribution...")
    plot_degree_distribution(sg)
    
    print("2. Generating network layout plot (sampled)...")
    save_graph_image(sg)
    
    print("3. Detecting communities...")
    num_comm = detect_communities(sg)
    print(f"   Detected {num_comm} communities.")
    
    print("4. Calculating Small-World properties...")
    avg_c, rand_c = analyze_small_world(sg)
    print(f"   Clustering Coefficient (Actual): {avg_c:.4f}")
    print(f"   Clustering Coefficient (Random Graph): {rand_c:.4f}")
    
    print("5. Predicting future links (Top 5 Jaccard)...")
    predictions = predict_future_links(sg)
    for u, v, score in predictions:
        print(f"   Link: ({u} <-> {v}) with Jaccard Score: {score:.4f}")

    print("\nAll tasks completed successfully! Check the 'benchmarks' directory for plots.")

if __name__ == "__main__":
    main()
