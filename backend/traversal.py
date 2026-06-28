from collections import deque
from graph_loader import Graph


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    print("\nBFS Traversal:")

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbour, _ in graph.graph.get(node, []):
                if neighbour not in visited:
                    queue.append(neighbour)


def dfs(graph, start):
    visited = set()

    print("\nDFS Traversal:")

    def dfs_visit(node):
        visited.add(node)
        print(node, end=" ")

        for neighbour, _ in graph.graph.get(node, []):
            if neighbour not in visited:
                dfs_visit(neighbour)

    dfs_visit(start)


if __name__ == "__main__":
    city = Graph()
    city.load_csv("roads.csv")

    bfs(city, "N0_0")
    print()
    dfs(city, "N0_0")