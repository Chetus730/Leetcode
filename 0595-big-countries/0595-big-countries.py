import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    fil_country= world[(world['area'] >= 3000000) | (world['population']>= 25000000)]
    return fil_country[['name','population','area']]