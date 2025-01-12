from typing import List, Dict, Any

def calculate_building_stress_index(readings: List[Dict[str, Any]]) -> float:
    """
    Calculate the Building Stress Index (BSI) based on temperature, humidity, and pressure variability.
    """
    if not readings:
        return 0.0

    # Initialize lists to store environmental parameters
    temperatures = []
    humidities = []
    pressures = []

    # Extract data from readings
    for r in readings:
        if 'temperature' in r and r['temperature'] is not None:
            temperatures.append(r['temperature'])
        if 'humidity' in r and r['humidity'] is not None:
            humidities.append(r['humidity'])
        if 'pressure' in r and r['pressure'] is not None:
            pressures.append(r['pressure'])

    # Calculate ranges
    temp_range = max(temperatures) - min(temperatures) if temperatures else 0.0
    hum_range = max(humidities) - min(humidities) if humidities else 0.0
    pres_range = max(pressures) - min(pressures) if pressures else 0.0

    # Weights for each parameter
    W_temp = 0.5
    W_hum = 0.3
    W_pres = 0.2

    # Calculate Building Stress Index
    BSI = (W_temp * temp_range) + (W_hum * hum_range) + (W_pres * pres_range)

    return BSI
