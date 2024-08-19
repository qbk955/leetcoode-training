import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    class_counts = courses.groupby('class').size()
    
    # Filtrowanie klas z co najmniej pięcioma studentami
    classes_with_min_students = class_counts[class_counts >= 5].index
    
    # Tworzenie DataFrame z klasami, które spełniają warunek
    result = pd.DataFrame({'class': classes_with_min_students})
    
    return result