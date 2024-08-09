import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
      
    df_sorted = employee.sort_values(by='salary', ascending=False).drop_duplicates(subset='salary')
    
    if df_sorted.shape[0] < 2:
            return pd.DataFrame({'SecondHighestSalary': [None]})
    
    second_highest = df_sorted.iloc[1]['salary']
    
    return pd.DataFrame({'SecondHighestSalary': [second_highest]})