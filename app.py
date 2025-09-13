import streamlit as st

st.title("Hello, Streamlit!")

st.sidebar.title("Características del modelo")
cement = st.sidebar.slider("Cemento", 0, 1000, 500)