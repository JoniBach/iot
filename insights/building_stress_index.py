"""
building_stress_index.py

For now, we return the difference between the max and min temperatures.
"""

from typing import List, Dict, Any

def calculate_building_stress_index(readings: List[Dict[str, Any]]) -> float:
    """
    Return the difference between the max temperature and the min temperature.
    """
    if not readings:
        return 0.0

    temps = [r.get("temperature") for r in readings if r.get("temperature") is not None]
    if not temps:
        return 0.0

    return max(temps) - min(temps)
