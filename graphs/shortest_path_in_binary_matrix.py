"""
Given an n x n binary matrix grid, return the length of the shortest clear
path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e.,
(0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e.,
they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path."""

from collections import deque


def shortest_path_binary_matrix(grid):

    # for shortest path use bfs
    n = len(grid)

    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1

    queue = deque([(0, 0, 1)])
    grid[0][0] = 1

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    while queue:
        r, c, dist = queue.popleft()

        if r == n - 1 and c == n - 1:
            return dist

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                grid[nr][nc] = 1
                queue.append((nr, nc, dist + 1))

    return -1


grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]

print(shortest_path_binary_matrix(grid))
# ans = 4

grid1 = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
print(shortest_path_binary_matrix(grid1))
# ans = -1
