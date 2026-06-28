import heapq
from .graph_loader import Graph
from .route_summary import generate_route_summary


def dijkstra(graph, start, destination):
    distances = {node: float("inf") for node in graph.graph}
    previous = {}

    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == destination:
            break

        for neighbour, weight in graph.graph[current_node]:
            distance = current_distance + weight

            if distance < distances.get(neighbour, float("inf")):
                distances[neighbour] = distance
                previous[neighbour] = current_node
                heapq.heappush(priority_queue, (distance, neighbour))

    path = []
    current = destination

    while current != start:
        path.append(current)
        current = previous[current]

    path.append(start)
    path.reverse()

    return path, distances[destination]


if __name__ == "__main__":
    city = Graph()
    city.load_csv("roads.csv")

    source = input("Enter Source: ")
    destination = input("Enter Destination: ")

    path, distance = dijkstra(city, source, destination)

    print("\nShortest Route")
    generate_route_summary(
    source,
    destination,
    path,
    distance
)