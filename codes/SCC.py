def dfs1(node,visited, stack, graph):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs1(neighbor, visited, stack, graph)
    stack.append(node)

def dfs2(node, visited, component, graph):
    visited.add(node)
    component.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs2(neighbor, visited, component, graph)


def kosaraju(graph):
    stack = []
    dfs1(0, set(), stack, graph)

    t_graph = [[] for _ in range(len(graph))]
    for node in range(len(graph)):
        for neighbor in graph[node]:
            t_graph[neighbor].append(node)

    sccs = []
    visited = set()
    while stack:
        node = stack.pop()
        if node not in visited:
            scc = []
            dfs2(node, visited, scc, t_graph)
            sccs.append(scc[:])
    return sccs

graph = [[1], [2, 4], [3, 5], [0, 6], [5], [4], [7], [5, 6]]
sccs = kosaraju(graph)
print("Strongly Connected Components:")
for scc in sccs:
    print(scc)