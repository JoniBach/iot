from typing import List, Dict, Any

# Import each insight function from its respective file
from insights.air_quality_index import calculate_air_quality_index
from insights.thermal_comfort_index import calculate_thermal_comfort_index
from insights.mold_risk_index import calculate_mold_risk_index
from insights.building_stress_index import calculate_building_stress_index
from insights.pressure_variance import calculate_pressure_variance
from insights.voc_exposure_score import calculate_voc_exposure_score

def get_insights_raw(readings: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Call all insight calculation functions and return their raw values as a dictionary.

    Args:
        readings (List[Dict[str, Any]]): List of sensor readings.

    Returns:
        Dict[str, float]: Dictionary containing raw values for each insight.
    """
    if not readings:
        raise ValueError("No sensor readings provided.")

    return {
        "air_quality_index": calculate_air_quality_index(readings),  # Ω
        "thermal_comfort_index": calculate_thermal_comfort_index(readings),  # °C
        "mold_risk_index": calculate_mold_risk_index(readings),  # %
        "building_stress_index": calculate_building_stress_index(readings),
        "pressure_variance": calculate_pressure_variance(readings),  # hPa
        "voc_exposure_score": calculate_voc_exposure_score(readings)  # Ω
    }
