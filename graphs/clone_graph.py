"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
"""

# using dfs and hashmap
from typing import Optional
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# doing it through dfs
def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
    clone_graph = {}

    def dfs(root):
        if not root:
            return None

        if root in clone_graph:
            return clone_graph[root]

        clone_graph[root] = Node(root.val, [])

        if root.neighbors:
            for neighbor in root.neighbors:
                clone_graph[root].neighbors.append(dfs(neighbor))

        return clone_graph[root]

    return dfs(node)


def clone_graph_bfs(node):
    if not node:
        return None

    clone_graph = {}
    bfs_queue = deque([node])

    clone_graph[node] = Node(node.val, [])
    while bfs_queue:
        curr = bfs_queue.popleft()

        if curr.neighbors:
            for nei in curr.neighbors:
                if nei not in clone_graph:
                    clone_graph[nei] = Node(nei.val, [])
                    bfs_queue.append(nei)
                clone_graph[curr].neighbors.append(clone_graph[nei])

    return clone_graph[node]
