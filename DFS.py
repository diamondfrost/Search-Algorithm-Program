# DFS ------------------------------------------------------------------------------------------------------------------

def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    print("Go to {} Node \n".format([start]))
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                print("Go to Node {} \n END".format([next]))
                yield path + [next]
            else:
                print("Go to Node {} \n".format([next]))
                stack.append((next, path + [next]))

# def dfs(graph, start, visited = None):
#     # visited, stack = set(), [start]
#     # while stack:
#     #     vertex = stack.pop()
#     #     if vertex not in visited:
#     #         visited.add(vertex)
#     #         stack.extend(graph[vertex] - visited)
#     # return visited
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     print("Go to {}".format(start))
#     for next in graph[start] - visited:
#         dfs(graph, next, visited)
#     return visited