import csv

def write_grid(n=5, spacing=300):
    rows = []

    def node(i, j):
        return f"N{i}_{j}"

    for i in range(n):
        for j in range(n):
            if j < n - 1:
                rows.append([node(i, j), node(i, j + 1), spacing])
                rows.append([node(i, j + 1), node(i, j), spacing])

            if i < n - 1:
                rows.append([node(i, j), node(i + 1, j), spacing])
                rows.append([node(i + 1, j), node(i, j), spacing])

    with open("backend/roads.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["source", "destination", "distance"])
        writer.writerows(rows)

    print("roads.csv created!")

if __name__ == "__main__":
    write_grid()