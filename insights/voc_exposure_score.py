"""
voc_exposure_score.py

For now, we return the minimum gas_resistance (Ω).
"""

from typing import List, Dict, Any

def calculate_voc_exposure_score(readings: List[Dict[str, Any]]) -> float:
    """
    Return the minimum gas_resistance (Ω).
    """
    if not readings:
        return 0.0

    gas_values = [r.get("gas_resistance") for r in readings if r.get("gas_resistance") is not None]
    if not gas_values:
        return 0.0

    return min(gas_values)
