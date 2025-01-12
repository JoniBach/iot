from typing import List, Dict, Any
import math

def calculate_pressure_variance(readings: List[Dict[str, Any]]) -> float:
    """
    Calculate the standard deviation of pressure readings (hPa).
    
    Args:
        readings (List[Dict[str, Any]]): List of sensor readings, each containing a 'pressure' key.
        
    Returns:
        float: Standard deviation of pressure readings. Returns 0.0 if insufficient data.
    """
    if not readings:
        return 0.0

    # Extract valid pressure readings
    pressures = [r.get("pressure") for r in readings if isinstance(r.get("pressure"), (int, float))]

    # Check if there are enough data points
    n = len(pressures)
    if n < 2:
        return 0.0

    # Calculate mean pressure
    mean_pressure = sum(pressures) / n

    # Calculate variance
    variance = sum((p - mean_pressure) ** 2 for p in pressures) / (n - 1)

    # Calculate standard deviation
    std_deviation = math.sqrt(variance)

    return std_deviation
