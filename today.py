from datetime import datetime, timedelta, timezone

def get_previous_day_range() -> tuple[str, str]:
    """
    Calculate the datetime range for the previous day (from midnight to midnight).

    Returns:
        tuple[str, str]: ISO 8601 formatted strings representing the start and end of the previous day.
    """
    # Get current UTC date and time
    current_date = datetime.now(timezone.utc)

    # Calculate the start and end of the previous day
    previous_day = current_date - timedelta(days=1)
    from_date = previous_day.replace(hour=0, minute=0, second=0, microsecond=0).isoformat()
    to_date = previous_day.replace(hour=23, minute=59, second=59, microsecond=0).isoformat()

    return from_date, to_date

if __name__ == "__main__":
    from_date, to_date = get_previous_day_range()
    print(f"Previous Day Range: {from_date} to {to_date}")
