import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    world_filter = world.loc[(world['area'] >= 3000000) | (world['population'] >= 25000000), :]
    world_filter = world_filter.drop(columns=['continent', 'gdp'])
    return world_filter