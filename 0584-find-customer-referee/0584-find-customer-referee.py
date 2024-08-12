import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    customer_mask = (customer['referee_id'] != 2) | (customer['referee_id'].isna())
    customer = customer[customer_mask]
    customer_final = customer[['name']]
    return customer_final