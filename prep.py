import warnings 
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
from util import get_db_url


def clean_data(df):
    df = df.dropna()
    df['bedroom'] = df['bedroom'].astype(int)
    df['fips'] = df['fips'].astype('int')
    df['home_value'] = df['home_value'].astype(int)
    df['square_feet'] = df['square_feet'].astype(int)

    return df

# This function delivers data that has been cleaned up.
# Nulls have been dropped.
# Data types have been changed to the appropriate data types.
