import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.preprocessing import scale

sns.set()

data = st.sidebar.radio('Choose which data.csv to use',['Insert your cleaned data.csv','Use pre-existing data.csv'])

if data == 'Insert your cleaned data.csv':

    uploaded = st.sidebar.file_uploader('Insert your data.csv')

    if uploaded != None:

        data = pd.read_csv(uploaded)
        df = data.copy()
        df_scaled = data.copy()

        x_axis = st.sidebar.selectbox('Select X-Axis',[columns for columns in df.columns])
        y_axis = st.sidebar.selectbox('Select Y-Axis',[columns for columns in df.columns])
        features = st.sidebar.multiselect('Select Features',[columns for columns in df.columns])
        standardize = st.sidebar.multiselect('Standardize',[columns for columns in df.columns])

        if standardize == [] and features != []:
            wcss = []
            
            for iter in range(1,int(len(df)*0.33)):
                kmeans = KMeans(iter)
                kmeans.fit(df[features])
                wcss.append(kmeans.inertia_)

            elbow_clusters = []
            
            for i,l in zip(wcss[1:], wcss):
                if i <= l*0.75:

                    elbow_clusters.append(wcss.index(i)+1)

                else:
                    break
            
            clusters = st.sidebar.select_slider('Select Number of Clusters',elbow_clusters, key=1)    

            fig, ax = plt.subplots(2,1, figsize=[7,10])

            ax[0].scatter(df[x_axis],df[y_axis])
            ax[0].title.set_text('Plot without Clusters')
            ax[0].set_ylabel(y_axis)

            kmeans = KMeans(clusters)
            kmeans.fit(df[features])

            df[str(clusters)+'_Clusters'] = kmeans.fit_predict(df[features])
            ax[1].scatter(df[x_axis],df[y_axis], c=df[str(clusters)+'_Clusters'], cmap='cool')
            ax[1].title.set_text('Plot with Clusters')
            ax[1].set_xlabel(x_axis)
            ax[1].set_ylabel(y_axis)

            st.pyplot(fig)

        elif standardize != [] and features != []:
            df_scaled[standardize] = scale(df_scaled[standardize])         
            wcss = []

            for iter in range(1,int(len(df)*0.33)):
                kmeans = KMeans(iter)
                kmeans.fit(df_scaled[features])
                wcss.append(kmeans.inertia_)

            elbow_clusters = []

            for i,l in zip(wcss[1:], wcss):
                if i <= l*0.75:

                    elbow_clusters.append(wcss.index(i)+1)

                else:
                    break
            
            clusters = st.sidebar.select_slider('Select Number of Clusters',elbow_clusters, key=2)    

            fig, ax = plt.subplots(1,2, figsize=[10,5])

            ax[0].scatter(df[x_axis],df[y_axis])
            ax[0].title.set_text('Original Plot without Clusters')
            ax[0].set_xlabel(x_axis)             
            ax[0].set_ylabel(y_axis)

            ax[1].scatter(df_scaled[x_axis],df_scaled[y_axis])
            ax[1].title.set_text('Scaled Plot without Clusters')
            ax[1].set_xlabel(x_axis)            
            ax[1].set_ylabel(y_axis)            

            st.pyplot(fig)            

            kmeans = kmeans_scaled = KMeans(clusters)
            kmeans.fit(df[features])
            kmeans_scaled.fit(df_scaled[features])

            fig, ax = plt.subplots(1,2, figsize=[10,5])

            df[str(clusters)+'_Clusters'] = kmeans.fit_predict(df[features])
            ax[0].scatter(df[x_axis],df[y_axis], c=df[str(clusters)+'_Clusters'], cmap='rainbow')
            ax[0].title.set_text('Original Plot with Clusters')
            ax[0].set_xlabel(x_axis)            
            ax[0].set_ylabel(y_axis)      

            df_scaled[str(clusters)+'_Clusters'] = kmeans_scaled.fit_predict(df_scaled[features])
            ax[1].scatter(df[x_axis],df[y_axis], c=df_scaled[str(clusters)+'_Clusters'], cmap='rainbow')
            ax[1].title.set_text('Scaled Plot with Clusters')
            ax[1].set_xlabel(x_axis)            
            ax[1].set_ylabel(y_axis)      

            st.pyplot(fig)

        else:
            st.write('Select Features')
                
else:

    data = pd.read_csv('Deployment/Clustering/Multi_clustering/loyalty_satisfaction.csv')
    df = data.copy()
    df_scaled = pd.DataFrame(scale(df), columns=df.columns)

    clusters = st.sidebar.select_slider('Select Number of Clusters',[2,3,4,5], key=2)
    
    def kmean(df,df_scaled,clusters):
        
        kmeans = kmeans_scaled = KMeans(clusters)
        kmeans.fit(df)
        kmeans_scaled.fit(df_scaled)

        df[str(clusters)+'_Clusters'] = kmeans.fit_predict(df)
        df_scaled[str(clusters)+'_Clusters'] = kmeans.fit_predict(df_scaled)
     
    kmeans = kmean(df,df_scaled,clusters)
    kmeans
    
    def plots(df, df_scaled, clusters):
    
        fig, ax = plt.subplots(2,1, figsize=[7,10])
        ax[0].scatter(df.iloc[:,0],df.iloc[:,1])
        ax[0].title.set_text('Plot without Clusters')
        ax[0].set_ylabel(df.columns[1])
        
        ax[1].scatter(df.iloc[:,0],df.iloc[:,1], c=df_scaled[str(clusters)+'_Clusters'], cmap='cool')
        ax[1].title.set_text('Plot with Clusters')
        ax[1].set_xlabel(df.columns[0])
        ax[1].set_ylabel(df.columns[1])       

        return fig
    
    subplot = plots(df, df_scaled, clusters)
    
    st.pyplot(subplot)
