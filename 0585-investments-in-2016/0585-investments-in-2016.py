import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    # Create a new column combining latitude and longitude
    insurance['latlon'] = insurance['lat'].astype(str) + ',' + insurance['lon'].astype(str)
    
    # Get counts of unique latlon values
    unique_latlon = insurance['latlon'].value_counts()
    
    # Filter for latlon values that occur exactly once
    unique_latlon = unique_latlon[unique_latlon == 1].index
    unique_cities = insurance[insurance['latlon'].isin(unique_latlon)]
    
    # Find rows with duplicate tiv_2015 values
    duplicate_tiv_2015 = insurance[insurance.duplicated('tiv_2015', keep=False)]
    
    # Merge on 'latlon' to get rows that meet both conditions
    result = pd.merge(duplicate_tiv_2015, unique_cities, on=['latlon'], suffixes=('_dup', '_unique'))
    
    # Check the columns in the result DataFrame
    print("Columns in result DataFrame:", result.columns)
    
    # Sum the tiv_2016 values
    if 'tiv_2016_unique' in result.columns:
        total_investment = result['tiv_2016_unique'].sum()
    else:
        total_investment = 0
    
    # Return the result as a DataFrame with the rounded sum
    return pd.DataFrame({'tiv_2016': [round(total_investment, 2)]})