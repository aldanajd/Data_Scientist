from ast import If
import streamlit as st
import matplotlib.pyplot as plt
import os 

upload = st.sidebar.file_uploader("Upload an image...", type=["jpg", "png"])
convert = 'python inference_realesrgan.py -n RealESRGAN_x4plus -i upload --outscale 3.5 --half --face_enhance'

if upload != None:

    os.system(convert)

    st.image(upload, caption='Original Image', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image(upload, caption='Upscale Image', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")