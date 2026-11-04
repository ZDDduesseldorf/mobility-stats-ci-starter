import csv
import os
from collections import defaultdict


def load_rides(p: str) -> list[dict[str, object]]:
    """Load ride data from a CSV file."""
    total_rides = []
    if os.path.exists(p) == False:
        raise FileNotFoundError(f"Could not find file: {p}")
    with open(p, newline="", encoding="utf-8") as f:
        ride_list = csv.DictReader(f)
        for rides in ride_list:
            rides.copy()
            total_rides.append(
                {
                    "ride_id": rides["ride_id"],
                    "start_station": rides["start_station"],
                    "end_station": rides["end_station"],
                    "duration_min": float(rides["duration_min"]),
                    "rider_type": rides["rider_type"],
                }
            )
    return total_rides


def average_duration(rides):
    """Return the average ride duration in minutes."""
    if len(rides) == 0:
        return 0.0
    total_duration = 0.0
    for ride in rides:
        total_duration += ride["duration_min"]
    return total_duration / len(rides)


def count_by_rider_type(rides):
    """Count rides for each rider type."""
    counts = defaultdict(int)
    for ride in rides:
        counts[ride["rider_type"]] += 1
    return dict(counts)


def busiest_start_station(rides):
    """Return the start station with the most rides."""
    if rides == None:
        raise ValueError("rides must not be None")
    if len(rides) == 0:
        raise ValueError("rides must not be empty")
    start_stations = {}
    for ride in rides:
        station = ride["start_station"]
        start_stations[station] = start_stations.get(station, 0) + 1
    return max(start_stations, key=start_stations.get)


def filter_long_rides(rides, duration=30):
    """Return all rides with duration greater than or equal to b minutes."""
    long_rides = []
    for ride in rides:
        if ride["duration_min"] >= duration:
            long_rides.append(ride)
    return long_rides
