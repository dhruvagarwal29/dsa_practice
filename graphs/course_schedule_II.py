"""There are a total of numCourses courses you have to take, labeled from 0
to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first
take course 1.
Return the ordering of courses you should take to finish all courses. If there
are many valid answers, return any of them. If it is impossible to finish all
courses, return an empty array.
"""

# using topological sort


from collections import defaultdict, deque


def course_schedule_II(numCourses, prerequisites):
    # count the indegrees and make the graph
    course_graph = defaultdict(list)
    in_degrees = [0] * numCourses

    for course, pre in prerequisites:
        course_graph[pre].append(course)
        in_degrees[course] += 1

    bfs_queue = deque()

    for i in range(numCourses):
        if in_degrees[i] == 0:
            bfs_queue.append(i)
    taken = 0
    res = []
    while bfs_queue:
        curr = bfs_queue.popleft()
        res.append(curr)
        taken += 1
        for nei in course_graph[curr]:
            in_degrees[nei] -= 1
            if in_degrees[nei] == 0:
                bfs_queue.append(nei)
    if taken == numCourses:
        return res
    return []


# numCourses = 2
# prerequisites = [[1, 0]]

# print(course_schedule_II(numCourses, prerequisites))


# numCourses = 4
# prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

# print(course_schedule_II(numCourses, prerequisites))


def course_schedule_II_dfs(numCourses, prerequisites):
    # make the course map
    course_map = defaultdict(list)
    for course, pre in prerequisites:
        course_map[pre].append(course)

    visited = set()
    visiting = set()
    result = []

    def dfs(course):
        if course in visited:
            return True

        if course in visiting:
            return False

        visiting.add(course)

        for nei in course_map[course]:
            if not dfs(nei):
                return False

        visiting.remove(course)
        visited.add(course)
        result.append(course)

        return True

    for i in range(numCourses):
        if not dfs(i):
            return []

    return result[::-1]


numCourses = 2
prerequisites = [[1, 0]]

print(course_schedule_II_dfs(numCourses, prerequisites))


numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

print(course_schedule_II_dfs(numCourses, prerequisites))
