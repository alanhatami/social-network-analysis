from collections import deque

def bfs_shortest_path(graph_obj, start_node, target_node):
    if start_node == target_node:
        return [start_node]

    queue = deque([[start_node]])
    visited = {start_node}

    while queue:
        path = queue.popleft()
        node = path[-1]

        for neighbor in graph_obj.graph[node]:
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                visited.add(neighbor)

                if neighbor == target_node:
                    return new_path
    return None

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