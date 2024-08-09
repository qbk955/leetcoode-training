import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df_merged = employee.merge(employee, left_on = 'managerId', right_on ='id', suffixes =('_emp', '_mng'))
    result = df_merged[df_merged['salary_emp'] > df_merged['salary_mng']]
    result = result[['name_emp']].rename(columns={'name_emp': 'Employee'})
    return result