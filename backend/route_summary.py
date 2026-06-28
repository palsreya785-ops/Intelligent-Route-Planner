def generate_route_summary(source, destination, path, distance):
    # Assume average speed = 40 km/h
    speed_kmph = 40
    speed_mps = (speed_kmph * 1000) / 3600

    travel_time = distance / speed_mps

    print("\n" + "=" * 50)
    print("          INTELLIGENT ROUTE PLANNER")
    print("=" * 50)

    print(f"Source          : {source}")
    print(f"Destination     : {destination}")
    print(f"Shortest Route  : {' -> '.join(path)}")
    print(f"Total Distance  : {distance} meters")
    print(f"Estimated Time  : {travel_time:.1f} seconds")
    print(f"Stops           : {len(path)-1}")

    print("=" * 50)