"""
mold_risk_index.py

For now, we simply take the average humidity (%).
"""

from typing import List, Dict, Any

def calculate_mold_risk_index(readings: List[Dict[str, Any]]) -> float:
    """
    Return the average humidity (%).
    """
    if not readings:
        return 0.0

    total_hum = 0.0
    count = 0

    for r in readings:
        hum_val = r.get("humidity")
        if hum_val is not None:
            total_hum += hum_val
            count += 1

    if count == 0:
        return 0.0

    return total_hum / count
