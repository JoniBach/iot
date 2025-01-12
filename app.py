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


def main():
    """
    Main execution function that orchestrates the fetching of readings and logging insights.
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
    else:
        print("No data found or an error occurred.")


if __name__ == "__main__":
    main()
