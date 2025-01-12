from typing import List, Dict, Any

def calculate_mold_risk_index(readings: List[Dict[str, Any]]) -> float:
    """
    Calculate the Mold Risk Index based on the percentage of time
    environmental conditions are favorable for mold growth.
    
    Args:
        readings (List[Dict[str, Any]]): List of sensor readings with 'temperature' and 'humidity'.
        
    Returns:
        float: Mold Risk Index ranging from 0 (no risk) to 100 (high risk).
    """
    if not readings:
        return 0.0

    # Thresholds for mold growth
    RH_THRESHOLD = 80.0  # Relative Humidity threshold (%)
    T_MIN = 5.0          # Minimum temperature for mold growth (°C)
    T_MAX = 40.0         # Maximum temperature for mold growth (°C)

    favorable_conditions_count = 0

    for reading in readings:
        temperature = reading.get('temperature')
        humidity = reading.get('humidity')

        if temperature is not None and humidity is not None:
            if T_MIN <= temperature <= T_MAX and humidity >= RH_THRESHOLD:
                favorable_conditions_count += 1

    total_readings = len(readings)
    if total_readings == 0:
        return 0.0

    # Calculate the percentage of time favorable conditions were present
    favorable_percentage = (favorable_conditions_count / total_readings) * 100

    return favorable_percentage
