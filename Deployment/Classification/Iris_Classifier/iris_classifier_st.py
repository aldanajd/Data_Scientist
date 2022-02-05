from matplotlib import get_backend
import pandas as pd
import numpy as np
import streamlit as st
import joblib

rfc = joblib.load('Deployment/Classification/Iris_Classifier/iris_rfc.pkl')
gbc = joblib.load('Deployment/Classification/Iris_Classifier/iris_gbc.pkl')
lr = joblib.load('Deployment/Classification/Iris_Classifier/iris_lr.pkl')


st.write("""
# Iris Flower Classifier
""")

st.sidebar.header('Select the stats of the flower')

def user_inputs():

    model = st.sidebar.selectbox("Select the Model to Use for Predictions", ['Random Forest Classifier', 'Gradient Boosting Classifier', 'Logistic Regression'], key=None)
    SepalLengthCm = st.sidebar.slider('Sepal Length (Cm)', min_value=0.0, max_value=15.0, value=5.0, step=0.1, key=None)
    SepalWidthCm = st.sidebar.slider('Sepal Width Cm', min_value=0.0, max_value=15.0, value=5.0, step=0.1, key=None)
    PetalLengthCm = st.sidebar.slider('Petal Length (Cm)', min_value=0.0, max_value=15.0, value=5.0, step=0.1, key=None)
    PetalWidthCm = st.sidebar.slider('Petal Width (Cm)', min_value=0.0, max_value=15.0, value=5.0, step=0.1, key=None)
    st.header('Prediction by ' + model, anchor=None)

    features = pd.DataFrame(np.array([SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]).reshape(1, -1), columns=['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm'])

    if model == 'Random Forest Classifier':
        model = rfc

    elif model == 'Gradient Boosting Classifier':
        model = gbc
    
    else:
        model = lr

    return pd.io.formats.style.Styler(pd.DataFrame(model.predict_proba(features), columns = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']), precision=2).highlight_max(axis=0)

user_inputs = user_inputs()

st.dataframe(data=user_inputs, width=None, height=None)
