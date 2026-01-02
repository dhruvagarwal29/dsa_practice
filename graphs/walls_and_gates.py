"""
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647
to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If
it is impossible to reach a gate, it should be filled with INF.
"""

from collections import deque


def wallsAndGates(rooms):
    rows = len(rooms)
    cols = len(rooms[0])

    # put gates in the queue
    queue = deque()

    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                queue.append((r, c))

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == 2147483647:
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append((nr, nc))

    return rooms


print(
    wallsAndGates(
        [
            [2147483647, -1, 0, 2147483647],
            [2147483647, 2147483647, 2147483647, -1],
            [2147483647, -1, 2147483647, -1],
            [0, -1, 2147483647, 2147483647],
        ]
    )
)

# answer should be [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
