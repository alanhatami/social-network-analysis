import collections
import csv

class SocialGraph:
    def __init__(self):
        self.graph = collections.defaultdict(list)
        self.nodes = set()

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.add(node)
            if node not in self.graph:
                self.graph[node] = []

    def add_edge(self, u, v):
        self.add_node(u)
        self.add_node(v)
        if v not in self.graph[u]:
            self.graph[u].append(v)
        if u not in self.graph[v]:
            self.graph[v].append(u)

    def load_from_csv(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader, None)
                for row in reader:
                    if len(row) >= 2:
                        try:
                            self.add_edge(int(row[0]), int(row[1]))
                        except ValueError:
                            continue
            return True
        except FileNotFoundError:
            return False