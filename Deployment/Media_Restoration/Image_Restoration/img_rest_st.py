import streamlit as st
import os 

upload = st.sidebar.file_uploader("Upload an image...", type=["jpg", "png"])
#convert = 'pip install realesrgan'

if upload != None:

    #os.system(convert)

    st.image(upload, caption='Original Image', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image(upload, caption='Upscale Image', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
