from typing import List, Dict, Any
import math

def calculate_air_quality_index(readings: List[Dict[str, Any]]) -> float:
    """
    Calculate the Air Quality Index (AQI) based on gas resistance and humidity.
    """
    if not readings:
        return 0.0

    # Constants for humidity compensation
    ph_slope = 0.04  # Example slope factor; adjust based on calibration
    gas_ceil = 50000  # Ceiling value for gas resistance normalization; adjust as needed

    # Initialize sums for averaging
    total_comp_gas = 0.0
    count = 0

    for r in readings:
        gas_res = r.get("gas_resistance")
        humidity = r.get("humidity")
        temperature = r.get("temperature")

        if gas_res is not None and humidity is not None and temperature is not None:
            # Calculate absolute humidity (in g/m³)
            abs_humidity = calculate_absolute_humidity(temperature, humidity)

            # Compensate gas resistance based on humidity
            comp_gas = gas_res * math.exp(ph_slope * abs_humidity)

            total_comp_gas += comp_gas
            count += 1

    if count == 0:
        return 0.0

    # Average compensated gas resistance
    avg_comp_gas = total_comp_gas / count

    # Calculate AQI as a percentage of the ceiling value
    aqi = min((avg_comp_gas / gas_ceil) ** 2, 1) * 100

    return aqi

def calculate_absolute_humidity(temperature: float, relative_humidity: float) -> float:
    """
    Calculate absolute humidity from temperature and relative humidity.
    """
    # Constants for the calculation
    A = 6.1121  # hPa
    B = 17.368
    C = 238.88  # °C

    # Calculate saturation vapor pressure (in hPa)
    svp = A * math.exp((B * temperature) / (C + temperature))

    # Calculate actual vapor pressure (in hPa)
    avp = svp * (relative_humidity / 100.0)

    # Convert vapor pressure to absolute humidity (in g/m³)
    abs_humidity = (avp * 100) / (461.5 * (temperature + 273.15))

    # Convert from g/m³ to kg/m³ for consistency
    return abs_humidity / 1000
