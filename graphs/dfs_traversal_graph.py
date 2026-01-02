# dfs travesal of the graph


def dfs_graph(adj_list, start):

    visited = set()
    result = []

    def dfs(node):
        visited.add(node)
        result.append(node)

        for neighbour in adj_list[node]:
            if neighbour not in visited:
                dfs(neighbour)

    dfs(start)
    return result


adj_list = [[1, 2], [2], [3], []]

print(dfs_graph(adj_list, 0))


"""
Time & Space Complexity
Time: O(V + E)
Recursive DFS: O(V) (call stack)

DFS goes deep first, BFS goes level by level

DFS is good for:
Cycle detection
Connected components
Topological sort
"""
