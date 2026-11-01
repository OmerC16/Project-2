import streamlit as st

st.title("Information")
st.warning("Notes\n\n"
           "Orbital period (days) - The time it takes for a sattelite to complete one full orbit.\n\n"
           "Perihelion distance (AU) - The distance of the sattelite from the parental object it orbits, at its closest point to it.\n\n"
           "Aphelion distance (AU) - The distance of the sattelite from the parental object it orbits, at its farthest point from it."
        )

st.header("Model information")
st.write(
    "The AI model is a Linear Regression model that uses two features to predict the output.\n\n"
    "In this case, the model takes an input of the Perihelion distance and the Aphelion distance of the sattelite's orbit, and predicts the Orbital period of the sattelite."
)

st.header("Game explanation")
st.write(
    "The game includes two sliders that are used to supply the AI model with information, so it will be able to predict the orbital period.\n\n"
    "The distances that the user provided is then displayed, along with the orbital period prediction, in the green box under the sliders.\n\n"
    "In order to visualize the orbit that the user has created (with the information they provided), there is a graph under the information text box that shows the parental object and the sattelite's orbit around it (this visualization is not accurate).\n\n"
)
