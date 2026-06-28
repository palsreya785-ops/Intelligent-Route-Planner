from fastapi import FastAPI
from pydantic import BaseModel
from .graph_loader import Graph
from .router import dijkstra

app = FastAPI(title="Intelligent Route Planner")

city = Graph()
city.load_csv("roads.csv")

class RouteRequest(BaseModel):
    source: str
    destination: str

@app.get("/")
def home():
    return {"message": "Intelligent Route Planner API Running"}

@app.post("/route")
def route(req: RouteRequest):
    path, distance = dijkstra(city, req.source, req.destination)

    speed = 40
    time = distance / ((speed * 1000) / 3600)

    return {
        "route": path,
        "distance": distance,
        "time": round(time, 2)
    }