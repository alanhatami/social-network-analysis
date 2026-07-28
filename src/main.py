from graph_manager import SocialGraph
from algorithms import bfs_shortest_path
import os

def main():
    sg = SocialGraph()
    
    test_edges = [(1, 2), (2, 3), (3, 4), (1, 5), (5, 4)]
    for u, v in test_edges:
        sg.add_edge(u, v)
    
    print(f"Nodes in graph: {sg.nodes}")
    
    path = bfs_shortest_path(sg, 1, 4)
    print(f"Shortest path from 1 to 4: {path}")

if __name__ == "__main__":
    main()
