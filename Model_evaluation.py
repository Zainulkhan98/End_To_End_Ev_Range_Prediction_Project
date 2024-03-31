
from Zenml_Pipeline.Feature_engineering import split_step
import numpy as np
from zenml import step
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
import pandas as pd
from typing import Tuple


# Evaluating the model
@step
def evaluate(y_test: pd.Series, predictions:pd.Series ) -> Tuple[float,float,float,float]:
    R2_score = r2_score(y_test,predictions)
    MSE = mean_squared_error(y_test,predictions)
    RMSE = np.sqrt(mean_squared_error(y_test,predictions))
    MAE = mean_absolute_error(y_test,predictions)

    return R2_score,MSE,RMSE,MAE




