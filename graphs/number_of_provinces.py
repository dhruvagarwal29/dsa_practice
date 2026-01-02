# here we need to find the number of provinces or we can say number of connected components


def number_provinces(adj_list, start):
    # using dfs to solve this problem

    visited = set()
    result = 0

    def dfs_helper(node):
        visited.add(node)

        for neighbour in adj_list[node]:
            if neighbour not in visited:
                dfs_helper(neighbour)

    for i in range(len(adj_list)):
        if i not in visited:
            dfs_helper(i)
            result += 1

    return result


graph = {0: [1, 2], 1: [2], 2: [3], 3: [], 4: [5], 5: [6], 6: [7], 7: []}

print(number_provinces(graph, 0))
