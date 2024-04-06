import pandas as pd
from zenml import step


# Ingesting data from csv data source
@step(enable_cache=False)
def ingest_data(data_path:str) -> pd.DataFrame:
    dfl = pd.read_csv(data_path)
    data = pd.DataFrame(dfl.loc[:12000,:])  # limiting the data to 12000 rows for faster processing
    return data

# exactly 12000 rows, so that i could get a control on no. of unique values in being passed to x_train while modeling






