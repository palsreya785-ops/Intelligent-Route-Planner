import networkx as nx
import matplotlib.pyplot as plt
from graph_loader import Graph
from router import dijkstra

# Load graph
city = Graph()
city.load_csv("roads.csv")

# Create NetworkX graph
G = nx.Graph()

for node in city.graph:
    for neighbour, distance in city.graph[node]:
        G.add_edge(node, neighbour, weight=distance)

# User input
source = input("Enter Source: ")
destination = input("Enter Destination: ")

# Find shortest path
path, total_distance = dijkstra(city, source, destination)

# Graph layout
pos = nx.spring_layout(G, seed=42)

# Draw graph
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightblue",
    node_size=700,
    font_size=8
)

# Highlight shortest path
path_edges = list(zip(path[:-1], path[1:]))

nx.draw_networkx_edges(
    G,
    pos,
    edgelist=path_edges,
    edge_color="red",
    width=3
)

plt.title("Intelligent Route Planner")
plt.show()

print("\nShortest Path:")
print(" -> ".join(path))
print(f"Total Distance: {total_distance} meters")