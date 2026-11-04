from mobility_stats.rides import average_duration, busiest_start_station, count_by_rider_type


def build_summary(rides):
    """Build a compact dictionary with headline statistics."""
    summary = {
        "ride_count": len(rides),
        "average_duration": average_duration(rides),
        "rider_types": count_by_rider_type(rides),
    }
    if rides:
        summary["busiest_start_station"] = busiest_start_station(rides)
    else:
        summary["busiest_start_station"] = None
    return summary


def format_summary(summary):
    """Create a human-readable text summary."""
    title = "Mobility summary"
    line1 = f"Rides: {summary['ride_count']}"
    line2 = f"Average duration: {summary['average_duration']:.1f} min"
    line3 = f"Busiest start: {summary['busiest_start_station']}"
    return title + "\n" + line1 + "\n" + line2 + "\n" + line3
