import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders_count = orders.groupby(by="customer_number").size().reset_index(name="orders_count")
    orders_max = orders_count.sort_values(by='orders_count', ascending=False)
    return orders_max.head(1)[['customer_number']]
    