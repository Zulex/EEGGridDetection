import streamlit as st
from streamlit_image_comparison import image_comparison

st.set_page_config(page_title="Image-Comparison Example", layout="centered")

st.title("EEG Grid detection")
st.write(
    "This is for testing purpose."
)


imageName = "100.png"
box = "data/box/"
crop = "data/crop/"
cropPose = "data/cropPose/"
initial = "data/intial/"
super = "data/super/"
superPose = "data/superPose"


st.image(initial + imageName)

# render image-comparison
image_comparison(
    img1= crop + imageName,
    img2= super + imageName,
)

