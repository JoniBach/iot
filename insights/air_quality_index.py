"""
air_quality_index.py

For now, we simply take the average gas_resistance (in Ohms).
"""

from typing import List, Dict, Any

def calculate_air_quality_index(readings: List[Dict[str, Any]]) -> float:
    """
    Return the average gas_resistance (Ω).
    """
    if not readings:
        return 0.0

    total_gas_res = 0.0
    count = 0

    for r in readings:
        gas_val = r.get("gas_resistance")
        if gas_val is not None:
            total_gas_res += gas_val
            count += 1

    if count == 0:
        return 0.0

    return total_gas_res / count
