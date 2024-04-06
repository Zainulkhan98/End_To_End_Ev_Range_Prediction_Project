import streamlit as st
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from Columns import impute_col_most_freq, categorical_col_encoding, numerical_col_normalize, county, city, make, Model
from Feature_engineering import preprocess_data
import joblib

# def ensure_consistent_feature_names(data):
#     expected_names = joblib.load('expected_feature_names.joblib')  # Load from model training
#     missing_names = set(expected_names) - set(data.columns)
#     for name in missing_names:
#         data[name] = 0
#     data = data[expected_names]  # Rearrange columns
#     return data

def main():

    st.title('Ev_Range_Prediction_App')

    st.write('This app predicts the range of the Electric Vehicle using the following features:')

    columns = {
        'County': st.selectbox( 'County', county),
        'City': st.selectbox('City', city),
        'Postal Code': st.number_input('Postal Code', value=98022),
        'Model Year': st.number_input('Model Year', value=2012),
        'Make': st.selectbox('Make', make),
        'Model': st.selectbox('Model', Model),
        'Electric Vehicle Type': st.selectbox('Electric Vehicle Type', ['Battery Electric Vehicle (BEV)', 'Plug-in Hybrid Electric Vehicle (PHEV)']),
        'Clean Alternative Fuel Vehicle (CAFV) Eligibility': st.selectbox('Clean Alternative Fuel Vehicle (CAFV) Eligibility', ['Clean Alternative Fuel Vehicle Eligible',
                                                                                                                                'Not eligible due to low battery range','Eligibility unknown as battery range has not been researched']),
        'DOL Vehicle ID': st.number_input('DOL Vehicle ID', value=229764972),
        '2020 Census Tract': st.number_input('2020 Census Tract', value=530330),
    }

    if st.button('Predict'):
        st.write('Model is Predicting...')

        # Create a DataFrame from user input
        data = pd.DataFrame(columns, index=[0])

        # Load the fitted transformers
        impute = joblib.load('joblib_loaded/imputer.joblib')
        scaler = joblib.load('joblib_loaded/scaler.joblib')
        ohe = joblib.load('joblib_loaded/encoder.joblib')

        # Transform the data
        data[impute_col_most_freq] = impute.transform(data[impute_col_most_freq])
        data[numerical_col_normalize] = scaler.transform(data[numerical_col_normalize])

        # Transform categorical columns
        data_to_encode = data[categorical_col_encoding]
        encoded_data = ohe.transform(data_to_encode)
        encoded_df = pd.DataFrame(encoded_data, columns=ohe.get_feature_names_out(data_to_encode.columns))
        data = pd.concat([data, encoded_df], axis=1)
        data = data.drop(categorical_col_encoding, axis=1)

        # Ensure consistent feature names
        # try:
        #     data = ensure_consistent_feature_names(data)
        # except Exception as e:
        #     st.error(f"Error aligning feature names: {e}")
        #     return  # Exit function gracefully

        # Load the model
        try:
            model = joblib.load('joblib_loaded/model')
        except Exception as e:
            st.error(f"Error loading model: {e}")
            return  # Exit function gracefully

        # Predict using the model
        st.subheader('Predicting...')
        prediction = model.predict(data)
        try:
            prediction = int(prediction)
            st.write(f'Prediction: {prediction}')
        except Exception as e:
            st.error(f"Error predicting: {e}")
            return

if __name__ == '__main__':
    main()