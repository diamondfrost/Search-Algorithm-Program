# BFS ------------------------------------------------------------------------------------------------------------------

def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    print("Go to {} Node \n".format([start]))
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                print("Go to Node {} \n END".format([next]))
                yield path + [next]
            else:
                print("Go to Node {} \n".format([next]))
                queue.append((next, path + [next]))

# def bfs(graph, start):
#     visited, queue = set(), [start]
#     while queue:
#         vertex = queue.pop(0)
#         if vertex not in visited:
#             visited.add(vertex)
#             queue.extend(graph[vertex] - visited)
#     return visited
