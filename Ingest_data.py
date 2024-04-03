import pandas as pd
from zenml import step,pipeline


# Ingesting data from csv data source
@step
def ingest_data(data_path:str) -> pd.DataFrame:
    dfl = pd.read_csv(data_path)
    data = pd.DataFrame(dfl.loc[:10000,:])  # limiting the data to 10000 rows for faster processing
    return data








