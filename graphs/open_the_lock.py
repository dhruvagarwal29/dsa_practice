"""
You have a lock in front of you with 4 circular wheels.
Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'.
The wheels can rotate freely and wrap around: for example we can turn
'9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of
these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock,
return the minimum total number of turns required to open the lock, or -1 if it
is impossible.
"""

from collections import deque


def openLock(deadends, target):
    def neighbor(lock):
        res = []
        for i in range(4):
            digit = int(lock[i])
            for move in (-1, 1):
                new_digit = (digit + move) % 10
                new_state = lock[:i] + str(new_digit) + lock[i + 1 :]
                res.append(new_state)

        return res

    deadends = set(deadends)

    if "0000" in deadends:
        return -1

    bfs_queue = deque(["0000"])
    steps = 0

    while bfs_queue:
        for _ in range(len(bfs_queue)):
            curr_lock = bfs_queue.popleft()

            if curr_lock == target:
                return steps

            for nei in neighbor(curr_lock):
                if nei not in deadends:
                    deadends.add(nei)
                    bfs_queue.append(nei)
        steps += 1

    return -1


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"

print(openLock(deadends, target))
