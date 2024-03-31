import pandas as pd
from Zenml_Pipeline.Ingest_data import ingest_data
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from zenml import step
from Zenml_Pipeline.Columns import impute_col_most_freq,categorical_col_encoding
from typing import Tuple


@step
def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    try:
        imputer = SimpleImputer(strategy='most_frequent')  # Instantiate imputer object
        data[impute_col_most_freq] = imputer.fit_transform(data[impute_col_most_freq])  # Fit imputer object to the data

        ohe = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
        encoded_cols = pd.DataFrame(ohe.fit_transform(data[categorical_col_encoding]))
        encoded_cols.columns = ohe.get_feature_names_out(categorical_col_encoding)

        # Drop original categorical columns and concatenate encoded columns
        data = data.drop(columns=categorical_col_encoding)
        data = pd.concat([data, encoded_cols], axis=1)
        data = pd.DataFrame(data)

    except Exception as e:
        print(f"Error during preprocessing: {e}")
    return data


@step
def split_step(data: pd.DataFrame, test_size:float, target_column:str) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    columns_to_drop = [target_column, 'Base MSRP','VIN (1-10)','DOL Vehicle ID', 'Legislative District']
    X = data.drop(columns_to_drop, axis=1)
    Y = data[target_column]
    x_train,x_test,y_train,y_test = train_test_split(X, Y, test_size=test_size, random_state=42)
    return x_train, x_test, y_train, y_test

