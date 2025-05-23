import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(page_title="Polygon Predictor", layout="centered")
st.title("Superheroes Face Masking")

# Replace with your Render backend URL
BACKEND_URL = "https://polygon-fastapi.onrender.com/predict/"

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    if st.button("Predict Mask"):
        files = {"file": uploaded_file.getvalue()}
        try:
            response = requests.post(BACKEND_URL, files={"file": files['file']})
            if response.status_code == 200:
                result_img = Image.open(io.BytesIO(response.content))

                col1, col2 = st.columns(2)
                with col1:
                    st.image(uploaded_file, caption="Original Image", width=300)
                with col2:
                    st.image(result_img, caption="Masked Prediction", width=300)
            else:
                st.error(f"Prediction failed. Status code: {response.status_code}")
        except Exception as e:
            st.error(f"Error contacting backend: {e}")
