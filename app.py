import streamlit as st

st.set_page_config(
    page_title= "Age Prediction Project",
    layout= "wide"
)

page = st.sidebar.radio("Navigation", ["Homepage", "EDA", "Data Prediction", "Data Visualization"])
uploaded_file = st.sidebar.file_uploader("Import a picture", type=["jpg"])