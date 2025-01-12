from typing import List, Dict, Any

def calculate_individual_thermal_comfort_index(temperature: float, humidity: float) -> float:
    """
    Calculate the Thermal Comfort Index (Heat Index) given temperature and humidity.
    
    Args:
        temperature (float): Air temperature in degrees Celsius.
        humidity (float): Relative humidity in percentage.
        
    Returns:
        float: Thermal Comfort Index (Heat Index) in degrees Celsius.
    """
    # Convert temperature to Fahrenheit for calculation
    T = temperature * 9/5 + 32
    RH = humidity

    # Heat Index calculation using the formula from the National Weather Service
    HI = (
        -42.379 + 2.04901523 * T + 10.14333127 * RH
        - 0.22475541 * T * RH - 6.83783e-3 * T**2
        - 5.481717e-2 * RH**2 + 1.22874e-3 * T**2 * RH
        + 8.5282e-4 * T * RH**2 - 1.99e-6 * T**2 * RH**2
    )

    # Convert Heat Index back to Celsius
    thermal_comfort_index = (HI - 32) * 5/9
    return thermal_comfort_index

def calculate_thermal_comfort_index(readings: List[Dict[str, Any]]) -> float:
    """
    Calculate the average Thermal Comfort Index (Heat Index) from a list of readings.
    
    Args:
        readings (List[Dict[str, Any]]): List of sensor readings, each containing 'temperature' and 'humidity'.
        
    Returns:
        float: Average Thermal Comfort Index (Heat Index) in degrees Celsius.
    """
    if not readings:
        return 0.0

    total_thermal_comfort_index = 0.0
    count = 0

    for r in readings:
        temp = r.get("temperature")
        hum = r.get("humidity")
        if temp is not None and hum is not None:
            thermal_comfort_index = calculate_individual_thermal_comfort_index(temp, hum)
            total_thermal_comfort_index += thermal_comfort_index
            count += 1

    if count == 0:
        return 0.0

    return total_thermal_comfort_index / count
