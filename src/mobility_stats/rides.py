import csv
import os
from collections import defaultdict
from typing import Any


def load_rides(csv_path: str) -> list[dict[str, Any]]:
    """Load ride data from a CSV file."""
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Could not find file: {csv_path}")

    all_rides = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            all_rides.append(
                {
                    "ride_id": row["ride_id"],
                    "start_station": row["start_station"],
                    "end_station": row["end_station"],
                    "duration_min": float(row["duration_min"]),
                    "rider_type": row["rider_type"],
                }
            )
    return all_rides


def average_duration(rides: list[dict[str, Any]]) -> float:
    """Return the average ride duration in minutes."""
    if not rides:
        return 0.0

    total_duration = 0.0
    for ride in rides:
        total_duration += ride["duration_min"]
    return total_duration / len(rides)


def count_by_rider_type(rides: list[dict[str, Any]]) -> dict[str, int]:
    """Count rides for each rider type."""
    rider_counts = defaultdict(int)
    for ride in rides:
        rider_counts[ride["rider_type"]] += 1
    return dict(rider_counts)


def busiest_start_station(rides: list[dict[str, Any]]) -> str:
    """Return the start station with the most rides."""
    if rides is None:
        raise ValueError("rides must not be None")
    if not rides:
        raise ValueError("rides must not be empty")

    station_counts = {}
    for ride in rides:
        start_station = ride["start_station"]
        station_counts[start_station] = station_counts.get(start_station, 0) + 1
    return max(station_counts, key=station_counts.get)


def filter_long_rides(rides: list[dict[str, Any]], threshold: int = 30) -> list[dict[str, Any]]:
    """Return all rides with duration greater than or equal to threshold minutes."""
    long_rides = []
    for ride in rides:
        if ride["duration_min"] >= threshold:
            long_rides.append(ride)
    return long_rides
