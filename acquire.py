import warnings 
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
from util import get_db_url
from prep import clean_data

def get_data_from_sql():
    query='''
    SELECT bedroomcnt as bedroom, 
    bathroomcnt as bathroom, 
    calculatedfinishedsquarefeet as square_feet,
    taxamount as tax_amount, 
    taxvaluedollarcnt as home_value, 
    proptype.propertylandusedesc as property_type, 
    fips
    FROM properties_2017 AS prop
    JOIN predictions_2017 AS pred USING (parcelid)
    JOIN propertylandusetype AS proptype USING (propertylandusetypeid)
    WHERE (transactiondate >= '2017-05-01' AND transactiondate <= '2017-06-30')
    AND (propertylandusedesc = 'Single Family Residential')
    AND prop.bedroomcnt > 0
    AND prop.bathroomcnt > 0
    AND prop.taxvaluedollarcnt > 0
    AND prop.lotsizesquarefeet > 0
    ORDER BY fips;
    '''
    df = pd.read_sql(query, get_db_url('zillow'))
    return df 


def acquire_zillow():
    df = get_data_from_sql()
    df = clean_data(df)
    return df 

