import warnings 
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
from env import user, host, password

def wrangle_zillow():

    def get_db_url(db):
        return f'mysql+pymysql://{user}:{password}@{host}/{db}'

    query='''
    SELECT bedroomcnt as bedroom, 
    bathroomcnt as bathroom, 
    taxamount as tax_amount, 
    taxvaluedollarcnt as tax_value, 
    propertylandusetypeid as property_id, 
    proptype.propertylandusedesc as property_type, 
    fips, 
    pred.transactiondate as transaction_date 
    FROM properties_2017 AS prop
    JOIN predictions_2017 AS pred USING (parcelid)
    JOIN propertylandusetype AS proptype USING (propertylandusetypeid)
    WHERE (transactiondate >= '2017-05-01' AND transactiondate <= '2017-06-30')
    AND (propertylandusedesc = 'Single Family Residential')
    AND prop.bedroomcnt > 0
    AND prop.bathroomcnt > 0
    AND prop.taxvaluedollarcnt > 0
    ORDER BY fips;
    '''
    df = pd.read_sql(query, get_db_url('zillow'))

    df = df.dropna()
    df['bedroom'] = df['bedroom'].astype(int)
    df['property_id'] = df['property_id'].astype(int)
    df['fips'] = df['fips'].astype('int')
    df['tax_value'] = df['tax_value'].astype(int)

    return df
