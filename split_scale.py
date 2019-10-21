import warnings 
warnings.filterwarnings("ignore")
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, QuantileTransformer, PowerTransformer, RobustScaler, MinMaxScaler


# the function will take a dataframe and returns train and test dataframe split where 80% is in train, and 20% in test.

def split_my_data(df, train_pct=.80, random_state=123):
    train, test = train_test_split(df, train_size=train_pct, random_state=random_state)
    return train, test

# z-scores, removes mean and scales to unit variance. Takes in a train and test set of data, creates and fits a scaler to the train set, returns the scaler, train_scaled, test_scaled

def standard_scaler(train, test):
    scaler = StandardScaler(copy=True, with_mean=True, with_std=True).fit(train)
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return scaler, train_scaled, test_scaled

# Turns scaled data back to its original format.

def scale_inverse(scaler, train_scaler, test_scaler):
    train_unscaled = pd.DataFrame(scaler.inverse_transform(train_scaled), columns=train_scaled.columns.values).set_index([train.index.values])
    test_unscaled = pd.DataFrame(scaler.inverse_transform(test_scaled), columns=test_scaled.columns.values).set_index([test.index.values])
    return scaler, train, test

# Quantile transformer, non_linear transformation - uniform. Reduces the impact of outliers, smooths out unusual distributions. Takes in a train and test set of data, creates and fits a scaler to the train set, returns the scaler, train_scaled, test_scalexsd

def uniform_scaler(train, test):
    scaler = QuantileTransformer(n_quantiles=100, output_distribution='uniform', random_state=123, copy=True).fit(train)
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return scaler, train_scaled, test_scaled

# Transforms and then normalizes data. Takes in a train and test set, yeo_johnson allows for negative data, box_cox allows positive data only. Zero_mean, unit variance normalized train and test.

def gaussian_scaler(train, test):
    scaler = PowerTransformer(method='yeo-johnson', standardize=False, copy=True).fit(train)
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return scaler, train_scaled, test_scaled

# Transforms features by scaling each feature to a given range. Takes in train and test data and returns the scaler and train and test scaled within range. Sensitive to outliers.

def min_max_scaler(train, test):
    scaler = MinMaxScaler(copy=True, feature_range=(0,1)).fit(train)
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return scaler, train_scaled, test_scaled

# Scales features using stats that are robust to outliers by removing the median and scaling data to the IQR. Takes in train and test sets and returns the scaler and scaled train and test sets

def iqr_robust_scaler(train, test):
    scaler = RobustScaler(quantile_range=(25.0,75.0), copy=True, with_centering=True, with_scaling=True).fit(train)
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return scaler, train_scaled, test_scaled