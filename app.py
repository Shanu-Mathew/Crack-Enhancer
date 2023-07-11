import streamlit as st
import numpy as np

import os

from PIL import Image
from src.crackEnhancer import EnhanceImage
from src.utils import resized_frame


# Function to process the image
def process_image(image):
    processed_image = EnhanceImage(image)  
    
    return processed_image

def save_image_pil(image, filename):
    image.save(filename)

# Streamlit app
if __name__ == '__main__':
    st.markdown("<h1 style='text-align: center;'>Crack Image Enhancer</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>Upload an image and enhance the image by using M2GLD Algorithm and Otsu Thresholding Algorithm</h5>", unsafe_allow_html=True)

    # Upload image
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display original image
        original_image = Image.open(uploaded_file)
        resized_image=resized_frame(np.array(original_image))

        # Process the image
        processed_image = process_image(resized_image)
        processed_image_pil = Image.fromarray(processed_image)

        # Display processed image
        col1, col2 = st.columns(2)
        with col1:
            st.header("Original Image")
            st.image(resized_image,caption="Original Image", use_column_width=False)

        with col2:
            st.header("Processed Image")
            st.image(processed_image_pil,caption="Crack Enhanced Image", use_column_width=False)
            with st.spinner("Processing..."):
                save_image_pil(processed_image_pil, "enhanced_image.jpg")
            st.download_button(
                label="Download Image",
                data="enhanced_image.jpg",
                file_name="enhanced_image.jpg",
                mime="image/jpeg"
            )
            os.remove("enhanced_image.jpg")