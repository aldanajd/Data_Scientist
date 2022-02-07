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
    joblib.dump(KMeans(i).fit(df),i+'_kmeans.pkl')
    joblib.dump(KMeans(i).fit(df_scaled),i+'_kmeans_scaled.pkl')

df[str(clusters)+'_Clusters'] = kmeans.fit_predict(df)
df_scaled[str(clusters)+'_Clusters'] = kmeans.fit_predict(df_scaled)

fig, ax = plt.subplots(2,1, figsize=[7,10])
ax[0].scatter(df.iloc[:,0],df.iloc[:,1])
ax[0].title.set_text('Plot without Clusters')
ax[0].set_ylabel(df.columns[1])

ax[1].scatter(df.iloc[:,0],df.iloc[:,1], c=df_scaled[str(clusters)+'_Clusters'], cmap='cool')
ax[1].title.set_text('Plot with Clusters')
ax[1].set_xlabel(df.columns[0])
ax[1].set_ylabel(df.columns[1])       

st.pyplot(dig)
