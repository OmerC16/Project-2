import streamlit as st

info = st.Page("info.py", title="Info")
model = st.Page("model.py", title="Model")

st.navigation([info, model]).run()
