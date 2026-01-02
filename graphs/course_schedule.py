"""
There are a total of numCourses courses you have to take,
labeled from 0 to numCourses - 1. You are given an array
prerequisites where prerequisites[i] = [ai, bi] indicates
that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course
0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

"""

"""
SOlution
there are 2 ways to resolve this question, first we can use dfs after
making the graph then we can have 2 sets to check if the course is taken 
or not

2nd way is using topological sort, we can count indegrees and after that we can select 
each course to check if the course is taken or not, it will result in False 
if there is a cycle

"""

from collections import defaultdict, deque


def dfs_course(numCourses, prerequisites):
    # no prerequisites
    if not prerequisites:
        return True  # all courses can be taken

    # making graph dependency
    graph = defaultdict(list)

    for course, pre in prerequisites:
        graph[pre].append(course)

    visited = set()
    visiting = set()

    def dfs(course):
        if course in visited:
            return True

        if course in visiting:  # cycle detected, means course are interdependent
            return False

        visiting.add(course)

        for neighbour in graph[course]:
            if not dfs(neighbour):
                return False

        visiting.remove(course)

        visited.add(course)

        return True

    for i in range(numCourses):
        if not dfs(i):
            return False

    return True


def toplogical_sort_course(numCourses, prerequisites):
    if not prerequisites:
        return True

    graph = defaultdict(list)
    in_degrees = [0] * numCourses
    # making graph

    for course, pre in prerequisites:
        graph[pre].append(course)
        in_degrees[course] += 1

    queue = deque()

    for i in range(numCourses):
        if in_degrees[i] == 0:
            queue.append(i)
    taken = 0
    while queue:
        curr = queue.popleft()
        taken += 1
        for neighbour in graph[curr]:
            in_degrees[neighbour] -= 1
            if in_degrees[neighbour] == 0:
                queue.append(neighbour)

    return numCourses == taken


numCourses = 2
prerequisites = [[1, 0], [0, 1]]

print(dfs_course(numCourses, prerequisites))
print(toplogical_sort_course(numCourses, prerequisites))

numCourses = 2
prerequisites = [[1, 0]]

print(dfs_course(numCourses, prerequisites))
print(toplogical_sort_course(numCourses, prerequisites))
