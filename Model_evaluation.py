
from Feature_engineering import split_step
import numpy as np
from zenml import step
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
import pandas as pd
from typing import Tuple
import mlflow
from Modeling import experiment_tracker

# Evaluating the model
@step(experiment_tracker=experiment_tracker.name)
def evaluate(y_test: pd.Series, predictions:pd.Series ) -> Tuple[float,float,float,float]:
    R2_score = r2_score(y_test,predictions) # try making r2_score class, if gives error
    mlflow.log_metric("R2_score", R2_score)
    MSE = mean_squared_error(y_test,predictions)
    mlflow.log_metric("MSE", MSE)
    RMSE = np.sqrt(mean_squared_error(y_test,predictions))
    mlflow.log_metric("RMSE", RMSE)
    MAE = mean_absolute_error(y_test,predictions)
    mlflow.log_metric("MAE", MAE)

    return R2_score,MSE,RMSE,MAE




