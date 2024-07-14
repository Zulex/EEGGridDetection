import streamlit as st
from streamlit_image_comparison import image_comparison

st.set_page_config(page_title="Image-Comparison Example", layout="centered")

st.title("EEG Grid detection")
st.write("This is for testing purpose.")


imageName = "100.png"
box = "data/box/"
crop = "data/crop/"
cropPose = "data/cropPose/"
initial = "data/initial/"
super = "data/super/"
superPose = "data/superPose/"


st.write("The original image with the item detected and bounding boxed displayed.")
st.image(box + imageName)
st.write("The crop according to the bounding box.")
st.image(crop + imageName)

st.write("Super resolution")
# render image-comparison
image_comparison(
    img1= crop + imageName,
    img2= super + imageName,
)

st.write("Pose detection on super resolution. Displaying low res image also for reference")
# render image-comparison
image_comparison(
    img1= cropPose + imageName,
    img2= superPose + imageName,
)

