import math
from typing import List, Dict, Any

def compensate_gas_reading(gas_resistance: float, temperature: float, humidity: float) -> float:
    """
    Compensate gas resistance reading based on temperature and humidity.

    Args:
        gas_resistance (float): Raw gas resistance in Ohms.
        temperature (float): Ambient temperature in degrees Celsius.
        humidity (float): Relative humidity in percentage.

    Returns:
        float: Compensated gas resistance.
    """
    # Example compensation formula; adjust coefficients as needed
    compensated_gas = gas_resistance * (1 + 0.01 * (temperature - 25)) * (1 + 0.02 * (humidity - 50))
    return compensated_gas

def calculate_voc_exposure_score(readings: List[Dict[str, Any]]) -> float:
    """
    Calculate VOC exposure score using compensated gas resistance readings.

    Args:
        readings (List[Dict[str, Any]]): List of sensor readings, each containing
                                         'gas_resistance' (Ohms), 'temperature' (°C), and 'humidity' (%).

    Returns:
        float: Average VOC exposure score.
    """
    if not readings:
        return 0.0

    voc_scores = []
    for reading in readings:
        gas_resistance = reading.get("gas_resistance")
        temperature = reading.get("temperature")
        humidity = reading.get("humidity")
        if gas_resistance is not None and temperature is not None and humidity is not None:
            compensated_gas = compensate_gas_reading(gas_resistance, temperature, humidity)
            voc_score = math.log(compensated_gas)  # Simplified scoring; adjust as needed
            voc_scores.append(voc_score)

    if not voc_scores:
        return 0.0

    # Return the average VOC exposure score
    return sum(voc_scores) / len(voc_scores)
