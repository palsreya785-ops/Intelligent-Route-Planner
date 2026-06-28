import tkinter as tk
from tkinter import messagebox
from graph_loader import Graph
from router import dijkstra

# Load graph
city = Graph()
city.load_csv("roads.csv")

def find_route():
    source = source_entry.get().strip()
    destination = destination_entry.get().strip()

    try:
        path, distance = dijkstra(city, source, destination)

        speed = 40  # km/h
        time = distance / ((speed * 1000) / 3600)

        result.set(
            f"Shortest Route:\n{' -> '.join(path)}\n\n"
            f"Distance: {distance} meters\n"
            f"Estimated Time: {time:.1f} seconds"
        )

    except Exception:
        messagebox.showerror(
            "Error",
            "Invalid source or destination!"
        )

# Main Window
root = tk.Tk()
root.title("Intelligent Route Planner")
root.geometry("500x400")

title = tk.Label(
    root,
    text="Intelligent Route Planner",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

tk.Label(root, text="Source").pack()
source_entry = tk.Entry(root, width=30)
source_entry.pack()

tk.Label(root, text="Destination").pack()
destination_entry = tk.Entry(root, width=30)
destination_entry.pack()

tk.Button(
    root,
    text="Find Route",
    command=find_route,
    bg="green",
    fg="white"
).pack(pady=10)

result = tk.StringVar()

tk.Label(
    root,
    textvariable=result,
    justify="left",
    font=("Arial", 11)
).pack(pady=10)

root.mainloop()