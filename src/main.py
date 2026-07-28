from graph_manager import SocialGraph
from algorithms import bfs_shortest_path
from analyzer import get_network_analysis, save_graph_image

def main():
    print("--- Social Network Analysis System ---")
    
    sg = SocialGraph()
    test_edges = [(1, 2), (2, 3), (3, 4), (1, 5), (4, 5), (2, 4)]
    for u, v in test_edges:
        sg.add_edge(u, v)
    print(f"Graph initialized with {len(sg.nodes)} users.")

    start, end = 1, 4
    path = bfs_shortest_path(sg, start, end)
    print(f"Shortest path from {start} to {end}: {path}")

    centrality = get_network_analysis(sg)
    print(f"User Influence (Centrality): {centrality}")
    save_graph_image(sg)

if __name__ == "__main__":
    main()
