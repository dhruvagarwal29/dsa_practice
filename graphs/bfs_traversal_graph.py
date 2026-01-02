# we are going to traverse a graph using a bfs(breadth first search) technique also known as
# level wise traversal

# we need to find the nodes in the manner of the levels

"""
Docstring for graphs.bfs_traversal_graph

        1           Level 1 (only one node can be at level 1)   
       / \  
      2   3         Level 2
     /\   /\ 
    4  5 6  7       Level 3

    ans - 1(level1) 2 3(level2) 4 5 6 7(level3)

    we need to use queues in BFS- queues are FIFO (first in first out)
    we will traverse the nodes and put their children nodes in the queues
    then we will do the same with their children
            
"""
from collections import deque


def bfs_graph_traversal(adj_list, start):
    n = len(adj_list)
    visited = set()
    queue = deque([start])

    visited.add(start)
    result = []
    level = [-1] * n
    level[start] = 0
    while queue:
        node = queue.popleft()
        result.append((node, f"level -> {level[node]}"))

        for neighbour in adj_list[node]:
            if neighbour not in visited:
                queue.append(neighbour)
                level[neighbour] = level[node] + 1
                visited.add(neighbour)

    return result


graph = {0: [1, 2], 1: [2], 2: [3], 3: []}

print(bfs_graph_traversal(graph, 0))

# TC - O(V + E)
# SC - O(V)
