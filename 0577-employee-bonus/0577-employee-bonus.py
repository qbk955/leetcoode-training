import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    employee = employee.merge(bonus, on='empId', how='left')
    employee_mask = (employee['bonus'] < 1000) | (employee['bonus'].isna())
    final = employee[employee_mask]
    final = final[['name', 'bonus']]
    return final
