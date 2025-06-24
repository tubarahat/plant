import streamlit as st
from PIL import Image

# Sidebar
st.sidebar.title("🌱 Plant Disease Detection System")
app_mode = st.sidebar.selectbox("Select Page", ["HOME", "ABOUT", "DISEASE RECOGNITION"])

# Home Page
if app_mode == "HOME":
    st.title("🌿 Plant Disease Detection System")
    st.image("Detection.jpg", use_column_width=True, caption="Identify Plant Diseases Accurately")

# About Page
elif app_mode == "ABOUT":
    st.header("🌱 About the Project")
    st.write("""
    This is a dummy version of the Plant Disease Detection System.
    It allows you to upload a plant leaf image and gives a placeholder prediction.
    """)

# Disease Recognition Page
elif app_mode == "DISEASE RECOGNITION":
    st.header("🔍 Disease Recognition")
    st.subheader("Upload a plant leaf image to detect diseases")

    test_image = st.file_uploader("Choose an Image:", type=["jpg", "jpeg", "png"])

    if test_image:
        img = Image.open(test_image)
        st.image(img, caption="Uploaded Image", width=250)

        if st.button("Predict"):
            st.success("🌟 Model Prediction: **This is a healthy plant.**")
