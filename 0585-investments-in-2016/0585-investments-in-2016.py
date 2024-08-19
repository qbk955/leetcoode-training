import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    insurance['latlon'] = insurance['lat'].astype(str) + ',' + insurance['lon'].astype(str)
    unique_latlon = insurance['latlon'].value_counts()
    unique_latlon = unique_latlon[unique_latlon == 1].index
    unique_cities = insurance[insurance['latlon'].isin(unique_latlon)]
    duplicate_tiv_2015 = insurance[insurance.duplicated('tiv_2015', keep=False)]
    result = pd.merge(duplicate_tiv_2015, unique_cities, on=['latlon'], suffixes=('_dup', '_unique'))
    if 'tiv_2016_unique' in result.columns:
        total_investment = result['tiv_2016_unique'].sum()
    else:
        total_investment = 0
    
    return pd.DataFrame({'tiv_2016': [round(total_investment, 2)]})