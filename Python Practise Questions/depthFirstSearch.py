"""
Implement a depth-first search (DFS) algorithm on a graph.

"""

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs_util(self, v, visited):
        visited.add(v)

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)
    
    def dfs(self, v):
        visited = set()
        self.dfs_util(v, visited)

# example 

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Following is DFS from (starting from vertex 2)")
    g.dfs(2)