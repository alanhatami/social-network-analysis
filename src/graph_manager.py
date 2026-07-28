import collections
import csv

class SocialGraph:
    def __init__(self):
        self.graph = collections.defaultdict(list)
        self.nodes = set()

    def add_edge(self, u, v):
        if v not in self.graph[u]:
            self.graph[u].append(v)
        if u not in self.graph[v]:
            self.graph[v].append(u)
        self.nodes.add(u)
        self.nodes.add(v)

    def load_from_csv(self, file_path):
        try:
            with open(file_path, 'r') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    u, v = int(row[0]), int(row[1])
                    self.add_edge(u, v)
            print(f"Successfully loaded {len(self.nodes)} nodes.")
        except FileNotFoundError:
            print("Error: CSV file not found!")