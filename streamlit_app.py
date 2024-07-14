import streamlit as st
from streamlit_image_comparison import image_comparison
import os

st.set_page_config(page_title="Image-Comparison Example", layout="centered")

st.title("EEG Grid detection")
st.write("This page presents a visualization of our project aimed at estimating the depth of small, non-rigid objects. Please note that these are preliminary results and are not intended for real-world application. The images used are sourced from a single video session, and the AI models have been trained on synthetic data.")
st.write("I use three different models in three steps. First I detect the object and its bounding box. Secondly I increase the resolution and lastly I detect the individual points of interest.")


box = "data/box/"
crop = "data/crop/"
cropPose = "data/cropPose/"
initial = "data/initial/"
super = "data/super/"
superPose = "data/superPose/"

col1, col2, col3 = st.columns(3)



# Function to get the list of image names
def get_image_names(directory):
    return sorted([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])

# Get the image names
image_names = get_image_names(initial)

if 'current_index' not in st.session_state:
    st.session_state.current_index = 0


if 'imageName' not in st.session_state:
    st.session_state.imageName = "100.png"

# Function to update the index and handle bounds
def update_index(delta):
    st.session_state.current_index = (st.session_state.current_index + delta) % len(image_names)

def display_filename():
    filename = image_names[st.session_state.current_index]
    with col2:
        st.write(filename)

def next_quote():
    if st.session_state.current_index + 1 >= len(image_names):
        st.session_state.current_index = 0
    else:
        update_index(1)

def previous_quote():
    if st.session_state.current_index > 0:
        update_index(-1)



display_filename()



with col1:
    if st.button("⏮️ Previous", on_click=previous_quote):
        pass

with col3:
    if st.button("Next ⏭️", on_click=next_quote):
        pass

imageName = image_names[st.session_state.current_index]

st.write("The original image with the first model detecting the object and its bounding active.")
st.image(box + imageName, use_column_width=True)

st.write("The crop according to the bounding box. See the low amount of data in which the individual points of the object are barely visible.")
st.image(crop + imageName, width=720)



st.write("I use a custom trained super resolution model to increase the image resolution. As you can see, it works on some images and fails on most.")
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

