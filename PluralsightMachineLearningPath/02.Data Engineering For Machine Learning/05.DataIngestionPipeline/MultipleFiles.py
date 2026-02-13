# MultipleFiles.py

import pandas as pd
import requests
import json
import os

# STEP 1: Ingest CSV data
def ingest_csv(file_path):
    print("Ingesting CSV data...")
    # Read CSV file into a DataFrame
    df = pd.read_csv(file_path)
    return df

# STEP 2: Ingest local JSON data
def ingest_json(file_path):
    print("Ingesting JSON data...")
    # Load JSON data from file and convert it to a DataFrame
    with open(file_path, 'r') as file:
        data = json.load(file)
    df = pd.DataFrame(data)
    return df
    
# STEP 3: Ingest weather data from REST API
def ingest_api(api_url):
    print("Ingesting API data...")
    # Send GET request to the API and parse the JSON response
    response = requests.get(api_url, verify=False)
    data = response.json()
    # Extract 'hourly' key and convert to DataFrame
    hourly_data = pd.DataFrame(data['hourly'])
    return hourly_data

# STEP 4: Main pipeline function to coordinate ingestion and merging
def run_pipeline():
    # Define file paths and API endpoint
    csv_path = 'energy_efficiency.csv'
    json_path = 'building_meta.json'
    api_url = 'https://api.open-meteo.com/v1/forecast?latitude=40.7&longitude=-74.0&hourly=temperature_2m'

    # STEP 4.1: Load CSV data
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(script_dir, csv_path)

    csv_df = ingest_csv(csv_file)
    print(f"CSV Data Shape: {csv_df.shape}")

    # STEP 4.2: Load JSON data
    json_file = os.path.join(script_dir, json_path)
    json_df = ingest_json(json_file)
    print(f"JSON Data Shape: {json_df.shape}")

    # STEP 4.3: Load API data
    api_df = ingest_api(api_url)
    print(f"API Data Shape: {api_df.shape}")

    # STEP 4.4: Combine all datasets horizontally using index alignment
    ## on production, you can use pd.merge with joins on a certain ids.
    combined_df = pd.concat([csv_df, json_df, api_df], axis=1)
    print("Combined Data Preview:")
    print(combined_df.head())

    # STEP 4.5: Save combined dataset to a new CSV file
    combined_df.to_csv("combined_dataset.csv", index=False)
    print("✅ Merged dataset saved to combined_dataset.csv")

# Run the full pipeline
if __name__ == "__main__":
    run_pipeline()