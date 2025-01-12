import os
import sys
from datetime import datetime
from supabase import create_client, Client
from dotenv import load_dotenv
from typing import List, Dict, Any

from get_insights_raw import get_insights_raw  # Import the insights function

def load_env_variables() -> Dict[str, str]:
    """
    Load environment variables and return Supabase credentials.
    """
    load_dotenv()
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    if not url or not key:
        raise ValueError("SUPABASE_URL or SUPABASE_KEY is not set in the environment variables.")
    return {"url": url, "key": key}


def initialize_supabase(url: str, key: str) -> Client:
    """
    Initialize the Supabase client with the provided credentials.
    """
    return create_client(url, key)


def fetch_readings_within_range(supabase: Client, table_name: str, from_date: str, to_date: str) -> List[Dict[str, Any]]:
    """
    Fetch rows from the specified table within a given datetime range using the Supabase client.

    Args:
        supabase (Client): Supabase client instance.
        table_name (str): Name of the table to query.
        from_date (str): Start of the datetime range (inclusive).
        to_date (str): End of the datetime range (inclusive).

    Returns:
        List[Dict[str, Any]]: List of readings within the specified range.
    """
    response = supabase.table(table_name).select("*").gte("created_at", from_date).lte("created_at", to_date).execute()

    # Return data if available, otherwise return an empty list
    return response.data if response and response.data else []


def send_insights_to_database(supabase: Client, table_name: str, insights: Dict[str, float]) -> None:
    """
    Send calculated insights to the 'daily_insights_raw' table in the Supabase database.

    Args:
        supabase (Client): Supabase client instance.
        table_name (str): Name of the target database table.
        insights (Dict[str, float]): Dictionary containing insights to be inserted.
    """
    try:
        # Insert insights into the specified table
        response = supabase.table(table_name).insert(insights).execute()

        # Check if the response contains an error or data
        if response.data:
            print(f"Insights successfully inserted into '{table_name}'. Response: {response.data}")
        elif response.error:
            print(f"Failed to insert insights. Error: {response.error}")
        else:
            print("Unexpected response structure from Supabase API.")
    except Exception as e:
        print(f"An error occurred while inserting insights: {str(e)}")


def main():
    """
    Main execution function that orchestrates the fetching of readings, logging insights, and saving them.
    """
    if len(sys.argv) != 3:
        print("Usage: python app.py <from_date> <to_date>")
        print("Example: python app.py 2025-01-01T00:00:00Z 2025-01-02T00:00:00Z")
        sys.exit(1)

    from_date = sys.argv[1]
    to_date = sys.argv[2]

    # Validate datetime format
    try:
        datetime.fromisoformat(from_date.replace("Z", "+00:00"))
        datetime.fromisoformat(to_date.replace("Z", "+00:00"))
    except ValueError:
        print("Invalid datetime format. Use ISO 8601 format (e.g., 2025-01-01T00:00:00Z).")
        sys.exit(1)

    # Load environment variables
    credentials = load_env_variables()

    # Initialize Supabase client
    supabase = initialize_supabase(credentials["url"], credentials["key"])

    # Fetch readings within the specified range
    readings = fetch_readings_within_range(supabase, "readings", from_date, to_date)

    if readings:
        print(f"Total readings fetched: {len(readings)}")

        # Call get_insights_raw to calculate raw insights
        insights = get_insights_raw(readings)

        # Log the insights
        print("Raw Insights:")
        for key, value in insights.items():
            print(f"{key}: {value}")

        # Send insights to the 'daily_insights_raw' table
        send_insights_to_database(supabase, "daily_insights_raw", insights)
    else:
        print("No data found or an error occurred.")


if __name__ == "__main__":
    main()
