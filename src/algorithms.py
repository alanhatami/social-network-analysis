from collections import deque
import math
import random

def bfs_traversal(graph_obj, start_node):
    visited = []
    visited_set = {start_node}
    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        visited.append(node)
        for neighbor in graph_obj.graph.get(node, []):
            if neighbor not in visited_set:
                visited_set.add(neighbor)
                queue.append(neighbor)
    return visited

def bfs_shortest_path(graph_obj, start_node, target_node):
    if start_node == target_node:
        return [start_node]
    queue = deque([[start_node]])
    visited = {start_node}
    while queue:
        path = queue.popleft()
        node = path[-1]
        for neighbor in graph_obj.graph.get(node, []):
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                visited.add(neighbor)
                if neighbor == target_node:
                    return new_path
    return None

def dfs_traversal(graph_obj, start_node):
    visited = []
    visited_set = {start_node}
    stack = [start_node]
    while stack:
        node = stack.pop()
        visited.append(node)
        for neighbor in reversed(graph_obj.graph.get(node, [])):
            if neighbor not in visited_set:
                visited_set.add(neighbor)
                stack.append(neighbor)
    return visited

def dijkstra_shortest_path(graph_obj, start_node, target_node):
    distances = {node: math.inf for node in graph_obj.nodes}
    distances[start_node] = 0
    previous = {node: None for node in graph_obj.nodes}
    unvisited = set(graph_obj.nodes)
    while unvisited:
        current = min(unvisited, key=lambda node: distances[node])
        if distances[current] == math.inf or current == target_node:
            break
        unvisited.remove(current)
        for neighbor in graph_obj.graph.get(current, []):
            if neighbor in unvisited:
                alt = distances[current] + 1
                if alt < distances[neighbor]:
                    distances[neighbor] = alt
                    previous[neighbor] = current
    path = []
    curr = target_node
    if previous[curr] is not None or curr == start_node:
        while curr is not None:
            path.insert(0, curr)
            curr = previous[curr]
        return path
    return None