import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Title of the Streamlit App
st.title("Image Processing with Streamlit")

# Upload image
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Convert the uploaded file to an OpenCV image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    st.image(img, caption="Original Image", use_column_width=True)

    # Sidebar options
    st.sidebar.header("Image Processing Options")
    options = st.sidebar.radio("Select an operation:", ["None", "Grayscale", "Blur", "Edge Detection"])

    if options == "Grayscale":
        processed_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        st.image(processed_img, caption="Grayscale Image", use_column_width=True, channels="GRAY")

    elif options == "Blur":
        ksize = st.sidebar.slider("Kernel Size", min_value=1, max_value=20, value=5, step=1)
        processed_img = cv2.GaussianBlur(img, (ksize * 2 + 1, ksize * 2 + 1), 0)
        st.image(processed_img, caption="Blurred Image", use_column_width=True)

    elif options == "Edge Detection":
        threshold1 = st.sidebar.slider("Threshold1", 0, 255, 100)
        threshold2 = st.sidebar.slider("Threshold2", 0, 255, 200)
        edges = cv2.Canny(img, threshold1, threshold2)
        st.image(edges, caption="Edge Detection", use_column_width=True, channels="GRAY")

    else:
        st.write("Choose an operation from the sidebar.")
else:
    st.write("Please upload an image to get started!")
