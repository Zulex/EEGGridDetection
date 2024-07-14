import streamlit as st
from streamlit_image_comparison import image_comparison

st.set_page_config(page_title="Image-Comparison Example", layout="centered")

st.title("EEG Grid detection")
st.write("This page presents a visualization of our project aimed at estimating the depth of small, non-rigid objects. Please note that these are preliminary results and are not intended for real-world application. The images used are sourced from a single video session, and the AI models have been trained on synthetic data.")
st.write("We use three different models in three steps. First we detect the object and its bounding box. Secondly we increase the resolution and lastly we detect the individual points of interest.")


imageName = "100.png"
box = "data/box/"
crop = "data/crop/"
cropPose = "data/cropPose/"
initial = "data/initial/"
super = "data/super/"
superPose = "data/superPose/"


st.write("The original image with the first model detecting the object and its bounding active.")
st.image(box + imageName, width=720)

st.write("The crop according to the bounding box. See the low amount of data in which the individual points of the object are barely visible.")
st.image(crop + imageName, width=720)



st.write("We use a custom trained super resolution model to increase the image resolution. As you can see, it works on some images and fails on most.")
# render image-comparison
image_comparison(
    img1= crop + imageName,
    img2= super + imageName,
    width=720
)

st.write("Finally, using a custom trained keypoint detection model to detect individual points. These points are labeled. When the cables are detected correctly and the points of the circles align relatively well, we can assume the individual points are correctly labeled.")
# render image-comparison
image_comparison(
    img1= cropPose + imageName,
    img2= superPose + imageName,
    width=720
)

