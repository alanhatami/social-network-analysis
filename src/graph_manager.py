import collections

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

