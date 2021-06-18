"""
Cycle In Graph:

You're given a list of edges representing an unweighted, directed graph with at least one node.
Write a function that returns a boolean representing whether the given graph contains a cycle.
For the purpose of this question, a cycle is defined as any number of vertices, including just one vertex, that are connected in a closed chain.
A cycle can also be defined as a chain of at least one vertex in which the first vertex is the same as the last.
The given list is what's called an adjacency list, and it represents a graph.
The number of vertices in the graph is equal to the length of edges, where each index i in edges contains vertex i's outbound edges, in no particular order.
Each individual edge is represented by a positive integer that denotes an index (a destination vertex) in the list that this vertex is connected to.
Note that these edges are directed, meaning that you can only travel from a particular vertex to its destination,
 not the other way around (unless the destination vertex itself has an outbound edge to the original vertex).
Also note that this graph may contain self-loops. A self-loop is an edge that has the same destination and origin;
 in other words, it's an edge that connects a vertex to itself. For the purpose of this question, a self-loop is considered a cycle.
For a more detailed explanation, please refer to the Conceptual Overview section of this question's video explanation.

Sample Input
    edges = [
    [1, 3],
    [2, 3, 4],
    [0],
    [],
    [2, 5],
    [],
    ]
Sample Output
    true 
    // There are multiple cycles in this graph: 
    // 1) 0 -> 1 -> 2 -> 0
    // 2) 0 -> 1 -> 4 -> 2 -> 0
    // 3) 1 -> 2 -> 0 -> 1
    // These are just 3 examples; there are more.

https://www.algoexpert.io/questions/Cycle%20In%20Graph
"""


#
def cycleInGraph(edges):
    in_call_stack = [False] * len(edges)

    for index in range(len(edges)):
        if cycleInGraphHelper(index, edges, in_call_stack) == True:
            return True
    return False


def cycleInGraphHelper(edge, edges, in_call_stack):

    if in_call_stack[edge]:
        return True

    in_call_stack[edge] = True

    for idx in edges[edge]:
        if cycleInGraphHelper(idx, edges, in_call_stack) == True:
            return True

    in_call_stack[edge] = False

    return False


#
def cycleInGraph2(edges):
    visited = [False] * len(edges)
    in_call_stack = [False] * len(edges)

    for index in range(len(edges)):
        if not visited[index] and cycleInGraphHelper2(index, edges, visited, in_call_stack) == True:
            return True
    return False


def cycleInGraphHelper2(edge, edges, visited, in_call_stack):

    if visited[edge] and in_call_stack[edge]:
        return True
    elif visited[edge]:
        return  # prevent multiple visits

    visited[edge] = True
    in_call_stack[edge] = True

    for idx in edges[edge]:
        if cycleInGraphHelper2(idx, edges, visited, in_call_stack) == True:
            return True

    in_call_stack[edge] = False

    return False
