# anything that has nodes and edgs known as a Graph

"""
Docstring for graphs.intro

there are directed and undirected graphs
directed - where edges have direction from one node to another
undirected - where edges are bi-directional in nature from one node to another

cyclic graph - if start from one node and ends to the same node is known as cyclic in a
graphs

acyclic graph - if there is no cycle in the graph

DAG - directed acyclic graph

path - contain lots of vertexes/nodes and each of them are reachable
a node cannot appear twice in the path

degrees in the node
- degree of the node is, the number of nodes goes inside or outside from the node is
the degree of the node

Property of an undirected graph-
total degree of the graph = 2 * E (number of edges)

Degree in directed graoh -
Indegree - the number edges coming to the node is indegree
Outdegree - the number of edges going out from the node is outdegree

-----------------------------------------------------------------------
here so the input can be given in ways like,
they will give n,m (nodes, edges) and links between them (2,1, 2,3)

also to store graphs we use
1) matrix (adjacency matrix)
2) list (adjacency list)


"""


# how to make adjacenct matrix?
def adjacency_matrix(n):
    # number of nodes (n)

    # initialize adjacency matrix with zeros
    adj_matrix = [[0 for _ in range(n)] for _ in range(n)]

    # list of edges (u, v)
    edges = [(0, 1), (0, 2), (1, 2), (2, 3)]

    # fill the matrix
    for u, v in edges:
        adj_matrix[u][v] = 1  # use 1 to show an edge

    # print the matrix
    for row in adj_matrix:
        print(row)


adjacency_matrix(4)

# how to make adjacenct list?


def adjacency_list(n):
    # n - is no of nodes

    from collections import defaultdict

    adj_list = defaultdict(list)

    # list of edges (u, v)
    edges = [(0, 1), (0, 2), (1, 2), (2, 3)]

    # fill the matrix
    for u, v in edges:
        adj_list[u].append(v)

    print(dict(adj_list))


adjacency_list(3)


## connected components
"""
if the graph are not connected to each other but there nodes then they are 
known as connected components

so traverse all the components we use visited array, where we check if the 
node is visited or not
"""
