import joblib
from Feature_engineering import split_step
from zenml import step
import pandas as pd
from sklearn import tree
from zenml.client import Client
import mlflow.sklearn

# Fitting the model

experiment_tracker = Client().active_stack.experiment_tracker
@step(experiment_tracker = experiment_tracker.name, enable_cache=False)
def modeling(x_train:pd.DataFrame,y_train:pd.Series) -> tree.DecisionTreeRegressor:
    model = tree.DecisionTreeRegressor().fit(x_train,y_train)
    mlflow.sklearn.autolog(model)
    joblib.dump(model, 'joblib_loaded/model')
    return model


# Making predictions
@step(enable_cache=False)
def predict(model:tree.DecisionTreeRegressor,x_test:pd.DataFrame) -> pd.Series:
    pred = model.predict(x_test)
    predictions = pd.Series(pred)
    return predictions




