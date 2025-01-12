"""
thermal_comfort_index.py

For now, we simply take the average temperature (°C).
"""

from typing import List, Dict, Any

def calculate_thermal_comfort_index(readings: List[Dict[str, Any]]) -> float:
    """
    Return the average temperature (°C).
    """
    if not readings:
        return 0.0

    total_temp = 0.0
    count = 0

    for r in readings:
        temp_val = r.get("temperature")
        if temp_val is not None:
            total_temp += temp_val
            count += 1

    if count == 0:
        return 0.0

    return total_temp / count
