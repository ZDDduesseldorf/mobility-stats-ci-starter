import csv
import os
from collections import defaultdict


def load_rides(csv_path: str) -> list[dict[str, object]]:
    """Load ride data from a CSV file."""
    rides = []
    if os.path.exists(csv_path) == False:
        raise FileNotFoundError(f"Could not find file: {csv_path}")
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for ride in reader:
            ride.copy()
            rides.append(
                {
                    "ride_id": ride["ride_id"],
                    "start_station": ride["start_station"],
                    "end_station": ride["end_station"],
                    "duration_min": float(ride["duration_min"]),
                    "rider_type": ride["rider_type"],
                }
            )
    return rides


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
    station_counts = {}
    for ride in rides:
        station = ride["start_station"]
        station_counts[station] = station_counts.get(station, 0) + 1
    return max(station_counts, key=station_counts.get)


def filter_long_rides(rides, threshold=30):
    """Return all rides with duration greater than or equal to threshold minutes."""
    long_rides = []
    for ride in rides:
        if ride["duration_min"] >= threshold:
            long_rides.append(ride)
    return long_rides
