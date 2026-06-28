import csv

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination, distance):
        if source not in self.graph:
            self.graph[source] = []

        self.graph[source].append((destination, int(distance)))

    def load_csv(self, filename):
        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                self.add_edge(
                    row["source"],
                    row["destination"],
                    row["distance"]
                )

    def display(self):
        print("\nCity Graph\n")

        for node in sorted(self.graph):
            print(f"{node} -> {self.graph[node]}")


if __name__ == "__main__":
    city = Graph()

    city.load_csv("roads.csv")

    city.display()