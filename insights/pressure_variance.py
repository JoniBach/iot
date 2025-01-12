"""
pressure_variance.py

For now, we calculate the standard deviation of pressure (hPa).
"""

from typing import List, Dict, Any
import math

def calculate_pressure_variance(readings: List[Dict[str, Any]]) -> float:
    """
    Return the standard deviation of pressure (hPa).
    """
    if not readings:
        return 0.0

    pressures = [r.get("pressure") for r in readings if r.get("pressure") is not None]
    n = len(pressures)

    if n < 2:
        # Not enough data to compute SD
        return 0.0

    mean_pressure = sum(pressures) / n
    variance = sum((p - mean_pressure) ** 2 for p in pressures) / (n - 1)
    std_deviation = math.sqrt(variance)

    return std_deviation
