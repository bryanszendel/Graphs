
from graph import Graph

def earliest_ancestor(ancestors, starting_node=None):
    graph = Graph()
    for vertex in range(len(ancestors)):
        graph.add_vertex(ancestors[vertex][0])
        graph.add_vertex(ancestors[vertex][1])
    for relation in range(len(ancestors)):
        graph.add_edge(ancestors[relation][0], ancestors[relation][1])
    print(graph.vertices)
    lengthy = 0
    dis_node = [-1]
    final = [-1]
    for node in ancestors:
        dis_node = node[0]
        testing = graph.dfs(dis_node, starting_node)
        if dis_node is not None and testing is not None and dis_node != starting_node:
            if len(testing) > lengthy:
                lengthy = len(testing)
                final = testing
        else:
            pass
    print(final[0])
    return final[0]

testers = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(testers, 2)
