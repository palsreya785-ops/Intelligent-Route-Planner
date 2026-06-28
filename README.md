# Intelligent Route Planner Using Graph Algorithms

## Overview

The Intelligent Route Planner is a Data Structures and Algorithms (DSA) project developed in Python. It models a road network as a weighted graph and computes the shortest route between two locations using Dijkstra's Algorithm. The project also demonstrates graph traversal using BFS and DFS and provides a FastAPI-based API for route computation.

## Features

* Graph representation using an adjacency list
* Breadth-First Search (BFS)
* Depth-First Search (DFS)
* Dijkstra's Shortest Path Algorithm
* Route summary generation
* Graph visualization using NetworkX and Matplotlib
* FastAPI REST API with Swagger documentation
* Sample road network generation using CSV

## Technologies Used

* Python 3
* FastAPI
* Uvicorn
* NetworkX
* Matplotlib
* Pandas
* Pytest

## Project Structure

```
Intelligent-Route-Planner/
│
├── backend/
│   ├── app.py
│   ├── data_builder.py
│   ├── dynamics.py
│   ├── graph_loader.py
│   ├── gui.py
│   ├── multicriteria.py
│   ├── route_summary.py
│   ├── router.py
│   ├── traversal.py
│   ├── visualize.py
│   ├── roads.csv
│   └── requirements.txt
│
├── tests/
├── screenshots/
├── README.md
└── .gitignore
```

## Algorithms Used

* Breadth-First Search (BFS)
* Depth-First Search (DFS)
* Dijkstra's Algorithm

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Intelligent-Route-Planner.git
cd Intelligent-Route-Planner
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r backend/requirements.txt
```

## Running the Project

Generate the sample road network:

```bash
cd backend
python data_builder.py
```

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

Run graph traversal:

```bash
python traversal.py
```

Run shortest path:

```bash
python router.py
```

Run visualization:

```bash
python visualize.py
```

## Sample Output

* Displays BFS and DFS traversal
* Finds the shortest route using Dijkstra's Algorithm
* Shows total distance and estimated travel time
* Visualizes the graph and highlighted shortest path

## Future Improvements

* Live traffic simulation
* Interactive map interface
* GPS coordinate support
* Multiple route optimization criteria
* Real-world map integration

## Learning Outcomes

This project demonstrates practical implementation of graph data structures and shortest path algorithms while introducing API development with FastAPI and graph visualization.

## Author

Sreya Pal
