import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.write("""
# Car Price Prediction App
This app predicts the price of cars by stats
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    brand = st.sidebar.selectbox("Select the Car's Brand",['Audi', 'BWM', 'Mercedes-Benz', 'Mitsubishi', 'Renault', 'Toyota', 'Volkswagen'], key=1)
    body = st.sidebar.selectbox("Select the Car's Body", ['Hatch', 'Sedan', 'Vagon', 'Van', 'Other'], key=2)
    mileage = st.sidebar.number_input("Select the Car's Mileage", value=0, key=4)
    engine = st.sidebar.number_input("Select the Car's EngineV", value=2.0, key=5)
    engine_type = st.sidebar.selectbox("Select the Car's Engine Type", ['Diesel', 'Gas', 'Petrol', 'Other'], key=3)

    columns = ['Mileage', 'EngineV','Brand_BMW', 'Brand_Mercedes-Benz',
        'Brand_Mitsubishi', 'Brand_Renault', 'Brand_Toyota', 'Brand_Volkswagen',
        'Body_Hatch', 'Body_Other', 'Body_Sedan', 'Body_Vagon', 'Body_Van',
        'Engine Type_Gas', 'Engine Type_Other', 'Engine Type_Petrol']

    df_dummy = pd.DataFrame(data= [[0]*len(columns)],columns=columns)

    if brand != 'Audi':
        df_dummy['Brand_'+ str(brand)] = 1
    df_dummy['Body_'+ str(body)] = 1
    df_dummy['Mileage'] = mileage
    df_dummy['EngineV'] = engine
    if engine_type != 'Diesel': 
        df_dummy['Engine Type_'+ str(engine_type)] = 1

    return df_dummy

inputs = user_input_features()
cars_lr_model = joblib.load('cars_lr_model.pkl')
prediction = np.exp(cars_lr_model.predict(inputs))[0]
float_formatter = "{:.2f}".format

st.subheader('Prediction')
st.write(str(float_formatter(prediction)),'$')
