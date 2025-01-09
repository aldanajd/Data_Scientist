# Requirements
import pandas as pd
import numpy as np
import streamlit as st
import joblib

from pandas.io.formats.style import Styler

# Loading the trained models
rfc = joblib.load('Deployment/Classification/Iris_Classifier/iris_rfc.pkl')
gbc = joblib.load('Deployment/Classification/Iris_Classifier/iris_gbc.pkl')
lr = joblib.load('Deployment/Classification/Iris_Classifier/iris_lr.pkl')

# App Title 
st.write("\n# Iris Flower Classifier")

# Sidebar: Title
st.sidebar.header('Select the stats of the flower')

def user_inputs():
    # Sidebar: SelectBox for Model
    model = st.sidebar.selectbox( 
        "Select the Model to Use for Predictions"
        , ['Random Forest Classifier'
            , 'Gradient Boosting Classifier'
            , 'Logistic Regression'
          ]
        , key=None
    )
    
    # Sidebar: Slider for Sepal Lenght (Cm)
    SepalLengthCm = st.sidebar.slider(
        'Sepal Length (Cm)'
        , min_value=0.0
        , max_value=15.0
        , value=5.0
        , step=0.1
        , key=None
    )

    # Sidebar: Slider for Sepal Width (Cm)
    SepalWidthCm = st.sidebar.slider(
        'Sepal Width Cm'
    , min_value=0.0
    , max_value=15.0
    , value=5.0
    , step=0.1
    , key=None
    )

    # Sidebar: Slider for Petal Lenght (Cm)
    PetalLengthCm = st.sidebar.slider(
        'Petal Length (Cm)'
    , min_value=0.0
    , max_value=15.0
    , value=5.0
    , step=0.1
    , key=None
    )

    # Sidebar: Slider for Petal Width (Cm)
    PetalWidthCm = st.sidebar.slider(
        'Petal Width (Cm)'
    , min_value=0.0
    , max_value=15.0
    , value=5.0
    , step=0.1
    , key=None
    )

    # Sub-Title 
    st.header('Prediction by ' + model, anchor=None)

    # Row of values from User Input
    row_of_values = np.array([SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]).reshape(1, -1)

    # Create DataFrame
    features_df = pd.DataFrame(
        row_of_values
        , columns=['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']
    )

    # Model selected from user input
    if model == 'Random Forest Classifier':
        model = rfc

    elif model == 'Gradient Boosting Classifier':
        model = gbc
    
    else:
        model = lr

    # Target Variable
    predictions = model.predict_proba(features_df)
    predictions_df = pd.DataFrame(
        predictions
        , columns = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    )

    # Hightlight Max Value from DataFrame
    return Styler(
        predictions_df
        , precision=2
    ).highlight_max(axis=1)

user_inputs_data = user_inputs()

# Render the DataFrame on the App
st.dataframe(data=user_inputs_data, width=None, height=None)
