import streamlit as st
import os 
import platform

upload = st.sidebar.file_uploader("Upload an image...", type=["jpg", "png"])
convert = 'git clone https://github.com/xinntao/Real-ESRGAN.git'
convert2 = 'pip install realesrgan'

if upload != None:
    
    os.system(convert)
    os.system(convert2)

    st.image(upload, caption='Original Image', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image(upload, caption='Upscaled Image, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
