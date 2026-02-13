# Module 2, Clip 2: Multi-Source Data Ingestion

This module demonstrates how to ingest and combine data from multiple sources including CSV files, JSON files, and REST APIs.

## Files

- `MultipleFiles.py`: Main script for multi-source data ingestion
- `energy_efficiency.csv`: Building energy efficiency dataset
- `building_meta.json`: Building metadata in JSON format
- `combined_dataset.csv`: Final merged dataset from all sources

## What You'll Learn

- Multi-source data ingestion strategies
- Combining data from different formats
- API integration for real-time data
- Data merging and alignment techniques
- Building comprehensive datasets from multiple sources

## Key Concepts

### Multi-Source Data Pipeline
- **CSV Ingestion**: Loading structured data from CSV files
- **JSON Ingestion**: Processing semi-structured JSON data
- **API Integration**: Fetching real-time data from REST APIs
- **Data Merging**: Combining datasets from different sources

### Data Source Integration
- **Energy Efficiency Data**: Building performance metrics
- **Building Metadata**: Property characteristics and specifications
- **Weather Data**: Real-time weather information from Open-Meteo API
- **Temporal Alignment**: Matching data across different time periods

## Usage

```bash
python MultipleFiles.py
```

## Data Processing Pipeline

1. **CSV Data Loading**: Import energy efficiency dataset
2. **JSON Data Processing**: Load building metadata
3. **API Data Fetching**: Retrieve weather data for New York coordinates
4. **Data Merging**: Combine all datasets horizontally
5. **Export Results**: Save combined dataset to CSV

## Data Sources

### Energy Efficiency Dataset
- Building energy performance metrics
- Heating and cooling loads
- Energy efficiency ratings

### Building Metadata (JSON)
- Property characteristics
- Building specifications
- Construction details

### Weather Data (API)
- Real-time temperature data
- Hourly weather information
- Geographic coordinates (40.7°N, 74.0°W - New York area)

## API Integration

The script demonstrates:
- **Open-Meteo API**: Free weather data service
- **Parameter Construction**: Building API URLs with coordinates
- **Response Processing**: Converting JSON to pandas DataFrame
- **Error Handling**: Managing API responses and failures

## Data Merging Strategy

```python
# Horizontal concatenation using index alignment
combined_df = pd.concat([csv_df, json_df, api_df], axis=1)
```

## Dependencies

- `pandas`: Data manipulation and analysis
- `requests`: HTTP library for API calls
- `json`: JSON data processing

## Learning Outcomes

After completing this module, you'll understand:
- How to ingest data from multiple sources
- API integration techniques
- Data merging and alignment strategies
- Building comprehensive datasets
- Handling different data formats
- Real-time data integration
