"""
Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and
'0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting
adjacent lands horizontally or vertically. You may assume all four
edges of the grid are all surrounded by water.
"""

from typing import List


def numIslands(grid: List[List[str]]) -> int:  # type: ignore
    row = len(grid)
    col = len(grid[0])
    result = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == "0":
            return

        grid[r][c] = "0"

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(row):
        for c in range(col):
            if grid[r][c] == "1":
                result += 1
                dfs(r, c)

    return result


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
print(numIslands(grid))

# TC - O(R*C)
# SC - O(1)


#### BFS solution

from collections import deque


def num_islands_bfs(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    def bfs(r, c):
        queue = deque([(r, c)])
        visited[r][c] = True

        while queue:
            row, col = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = row + dr, col + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and not visited[nr][nc]
                    and grid[nr][nc] == "1"
                ):
                    visited[nr][nc] = True
                    queue.append((nr, nc))

    count = 0
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c] and grid[r][c] == "1":
                bfs(r, c)
                count += 1

    return count
