import os
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


def fetch_all_readings(supabase: Client, table_name: str) -> List[Dict[str, Any]]:
    """
    Fetch all rows from the specified table using the Supabase client.
    """
    response = supabase.table(table_name).select("*").execute()

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
    # Load environment variables
    credentials = load_env_variables()

    # Initialize Supabase client
    supabase = initialize_supabase(credentials["url"], credentials["key"])

    # Fetch readings from the 'readings' table
    readings = fetch_all_readings(supabase, "readings")

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
