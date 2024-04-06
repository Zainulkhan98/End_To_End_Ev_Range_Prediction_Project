# EV Range Prediction Project

This project is a machine learning pipeline that predicts the electric vehicle (EV) range based on various features. The project is implemented in Python and uses the ZenML pipeline framework for orchestrating the machine learning workflow. The project also uses MLflow for experiment tracking and model logging.

## Project Structure

The project is divided into several Python scripts, each responsible for a specific step in the machine learning pipeline:

- `Ingest_data.py`: This script is responsible for ingesting data from a CSV file. The data is limited to 12000 rows for faster processing.

- `Feature_engineering.py`: This script is not included in the provided context, but it presumably handles preprocessing and splitting of the data.

- `Modeling.py`: This script is responsible for training a Decision Tree Regressor model on the training data and making predictions on the test data.

- `Model_evaluation.py`: This script evaluates the model's performance using various metrics such as R2 score, Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and Mean Absolute Error (MAE).

- `run_pipeline.py`: This script orchestrates the entire pipeline, from data ingestion to model evaluation.

## How to Run

To run the pipeline, execute the `run_pipeline.py` script. Make sure to replace the `data_path` argument in the `ev_range_prediction_pipeline` function call with the path to your CSV file.

```python
ev_range_prediction_pipeline('path_to_your_data.csv')
```

## Dependencies

This project requires the following Python packages:

- pandas
- zenml
- numpy
- sklearn
- mlflow
- joblib

You can install these packages using pip:

```bash
To make prediction through streamlit
streamlit run streamlit_app.py
```

## Author

This project is developed by Zainulkhan98.
