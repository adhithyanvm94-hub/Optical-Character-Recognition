import streamlit as st
from PIL import Image
import pytesseract
import pyttsx3

# Set Tesseract path (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

st.title("OCR + Text-to-Speech")
st.write("Upload an image, extract text, and listen to it!")

# Upload image
uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_container_width=True)
    
    # Button to extract text
    if st.button("Convert Image to Text"):
        text = pytesseract.image_to_string(img)
        if text.strip() == "":
            st.warning("No text found in the image.")
        else:
            st.session_state['text'] = text
            st.subheader("Extracted Text:")
            st.write(text)
    
    # Button to convert text to audio
    if 'text' in st.session_state and st.button("Convert Text to Audio"):
        engine = pyttsx3.init()
        engine.say(st.session_state['text'])
        engine.runAndWait()
