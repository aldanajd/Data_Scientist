import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.preprocessing import scale

sns.set()

data = pd.read_csv('Deployment/Clustering/Multi_clustering/loyalty_satisfaction.csv')
df = data.copy()
df_scaled = pd.DataFrame(scale(df), columns=df.columns)

clusters = st.sidebar.select_slider('Select Number of Clusters',[2,3,4,5], key=2)

import joblib

kmeans = kmeans_scaled = KMeans(clusters)
kmeans_scaled.fit(df_scaled)

for i in [2,3,4,5]:
    joblib.dump(KMeans(i).fit(df),str(i)+'_kmeans.pkl')
    joblib.dump(KMeans(i).fit(df_scaled),str(i)+'_kmeans_scaled.pkl')
