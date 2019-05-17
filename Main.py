import BFS
import DFS
import DijkstraAlgorithm
import BellmanFordAlgorithm

# Main Function --------------------------------------------------------------------------------------------------------


# graph BFS DFS
mine = {"START": set(["A", "B", "C", "D"]),
        "A": set(["START", "A1", "A2"]),
        "B": set(["START", "B1"]),
        "C": set(["START", "C1"]),
        "D": set(["START", "D1", "D2"]),
        "A1": set(["A", "A3", "AB"]),
        "A2": set(["A", "A3", "AC"]),
        "A3": set(["A1", "A2"]),
        "B1": set(["B", "B11", "B12", "AB"]),
        "B11": set(["B1", "BD"]),
        "B12": set(["B1"]),
        "C1": set(["C11", "AC"]),
        "C11": set(["C1"]),
        "D1": set(["D", "BD"]),
        "D2": set(["D", "D21"]),
        "D21": set(["D2"])}


print("Available Mine Rooms: A, A1, A2, A3,"
      " B, B1, B11, B12,"
      " C, C11,"
      " D, D1, D2, D21"
      " AB, AC, BD\n")
algo = input("Input 1 for DFS, 2 for BFS, 3 for Dijkstra's Algorithm and 4 for Bellman-Ford's Algorithm: \n")

if (algo == "1"):
    GoldNode = input("Input where gold is: \n")
    dfs_path(mine, "START", GoldNode)
    DFS_path = list(dfs_path(mine, "START", GoldNode))
    print(DFS_path)

elif(algo == "2"):
    GoldNode = input("Input where gold is: \n")
    bfs_path(mine, "START", GoldNode)
    BFS_path = list(dfs_path(mine, "START", GoldNode))
    print(BFS_path)

elif (algo == "3"):
    StartNode = input("Input where to start: \n")
    GoldNode = input("Input where gold is: \n")
    print(DAgraph.dijkstra("A", "A1"))

elif(algo == "4"):
    StartNode = input("Input where to start: \n")
    GoldNode = input("Input where gold is: \n")
    print(BFAgraph.BellmanFord("A", "A1"))

else:
    print("Invalid Number!")

