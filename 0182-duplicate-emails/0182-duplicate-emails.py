import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicates = person[person.duplicated(subset='email')]
    duplicates = duplicates.drop(columns='id')
    duplicates = duplicates.drop_duplicates()
    
    return duplicates