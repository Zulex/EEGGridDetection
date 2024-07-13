import streamlit as st
from streamlit_image_comparison import image_comparison

st.set_page_config(page_title="Image-Comparison Example", layout="centered")

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/). Test"
)

# render image-comparison
image_comparison(
    img1="image1.jpg",
    img2="image2.jpg",
)

# render image-comparison
image_comparison(
    img1="image1.jpg",
    img2="image2.jpg",
)