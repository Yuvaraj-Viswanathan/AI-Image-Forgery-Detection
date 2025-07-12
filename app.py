import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import os
from resize_ela import convert_to_ela_image  # Make sure this file exists

# Title
st.set_page_config(page_title="AI Image Forgery Detection", layout="centered")
st.title("🔍 AI Image Forgery Detection Tool")

# Upload section
uploaded = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

# Load trained model
model_path = "models/ela_model.h5"
if os.path.exists(model_path):
    model = tf.keras.models.load_model(model_path)
else:
    st.error("Trained model not found! Please place 'ela_model.h5' in 'models/' folder.")
    st.stop()

# When user uploads image
if uploaded:
    with open("temp.jpg", "wb") as f:
        f.write(uploaded.read())

    st.image("temp.jpg", caption="Original Image", use_column_width=True)

    # Convert to ELA image
    try:
        ela_img = convert_to_ela_image("temp.jpg", "temp_ela.jpg")
        ela_img = ela_img.resize((224, 224))
        st.image(ela_img, caption="ELA Processed Image", use_column_width=True)
    except Exception as e:
        st.error(f"ELA Processing Failed: {str(e)}")
        st.stop()

    # Convert image to model input format
    img_array = np.array(ela_img).astype("float32") / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)[0][0]
    confidence = prediction if prediction > 0.5 else 1 - prediction

    if prediction > 0.5:
        st.error(f"🔴 Forged Image Detected (Confidence: {confidence:.2f})")
    else:
        st.success(f"🟢 Authentic Image (Confidence: {confidence:.2f})")
