from typing import Tuple
import joblib
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from zenml import step

from Columns import impute_col_most_freq, categorical_col_encoding, numerical_col_normalize

@step(enable_cache=False)
def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    try:
        # Drop unnecessary columns (consider feature importance analysis later)
        data = data.drop(['Base MSRP', 'VIN (1-10)', 'Vehicle Location', 'Legislative District', 'State', 'Electric Utility'], axis=1)

        # Impute missing values in specified columns
        imputer = SimpleImputer(strategy='most_frequent')
        data[impute_col_most_freq] = imputer.fit_transform(data[impute_col_most_freq])
        joblib.dump(imputer, 'joblib_loaded/imputer.joblib')

        # Standardize numerical columns
        scaler = StandardScaler()
        data[numerical_col_normalize] = scaler.fit_transform(data[numerical_col_normalize])
        joblib.dump(scaler, 'joblib_loaded/scaler.joblib')

        # One-hot encode categorical columns
        ohe = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
        data_to_encode = data[categorical_col_encoding]
        encoded_data = ohe.fit_transform(data_to_encode)
        joblib.dump(ohe, 'joblib_loaded/encoder.joblib')

        # Create DataFrame from encoded data with appropriate column names
        encoded_df = pd.DataFrame(encoded_data, columns=ohe.get_feature_names_out(data_to_encode.columns))

        # Concatenate the original data with the encoded data
        data = pd.concat([data, encoded_df], axis=1)

        # Drop the original categorical columns
        data = data.drop(categorical_col_encoding, axis=1)

        return data

    except Exception as e:
        print(f"Error during preprocessing: {e}")


@step(enable_cache=False)
def split_step(data: pd.DataFrame, test_size:float, target_column:str) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    columns_to_drop = [target_column, 'Base MSRP', 'Legislative District']
    X = data.drop(target_column, axis=1)
    Y = data[target_column]

    x_train = X.iloc[:10000,:]
    x_test = X.iloc[10000:,:]
    y_train = Y.iloc[:10000]
    y_test = Y.iloc[10000:]

    return x_train, x_test, y_train, y_test

