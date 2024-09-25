import base64
import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(layout="wide")

# Define Flask server URL
FLASK_SERVER_URL = "http://localhost:5000/process_image"

# Streamlit UI
st.title("Image to JSON Extractor")
st.write("Upload an image and the model will extract structured JSON data.")

uploaded_file = st.file_uploader(
    "Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert image to bytes
    image = Image.open(uploaded_file)
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='PNG')
    image_bytes = image_bytes.getvalue()

    # Encode image bytes to base64
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')
    with st.spinner("Processing image... Please wait."):
        response = requests.post(FLASK_SERVER_URL, json={
                                 'image': image_base64})

        
        col1, col2 = st.columns([1, 1])

        with col1:
            st.image(image, caption="Uploaded Image", use_column_width=False)

        with col2:
            if response.status_code == 200:
                generated_json = response.json()
                st.subheader("Extracted JSON Data")
                st.json(generated_json)
            else:
                st.error(f"Error: {response.status_code}")