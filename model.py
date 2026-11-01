import kagglehub
import pandas as pd
import os
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib.patches import Ellipse

KAGGLE_DATASET = "shrutimehta/nasa-asteroids-classification"
CSV_TABLE = "nasa.csv"
FEATURE_COLUMNS = ["Perihelion Distance", "Aphelion Dist"]
TARGET_COLUMN = "Orbital Period"
ORBIT_OBJECT_RADIUS = 0.35
CONST_X = 5
VERTICAL_DIST_MIN = 2.01 - 0.18
VERTICAL_DIST_MAX = 8.98 - 0.18
WIDTH_TO_HEIGHT_RATIO = 0.6

path = kagglehub.dataset_download(KAGGLE_DATASET)

csv_path = os.path.join(path, CSV_TABLE)
data = pd.read_csv(csv_path)

X = data[FEATURE_COLUMNS].to_numpy()
y = data[TARGET_COLUMN].to_numpy()

def mse_loss(y_true, y_predict):
  return np.mean((y_true - y_predict) ** 2)

X = data[FEATURE_COLUMNS].to_numpy()
model = LinearRegression()
model.fit(X, y)

y_hat = model.predict(X)
loss = mse_loss(y, y_hat)

st.title("Predict the orbital period by the Perihelion distance and the Aphelion distance")

perihelionDist = st.slider("Enter the Perihelion distance of the asteroid (AU):", 0.18, 1.3)
aphelionDist = st.slider("Enter the Aphelion distance of the asteroid (AU):", 2.01, 8.98)

st.success("Perihelion distance: " + str(perihelionDist) + "AU\n\nAphelion distance: " + str(aphelionDist) + "AU\n\nThe Orbital period is: " + str(np.round(model.predict(np.array([[perihelionDist, aphelionDist]])), 3)[0]) + " days")

verticalDist = aphelionDist + perihelionDist + 2 * ORBIT_OBJECT_RADIUS
maxY = verticalDist + 2
constY = maxY - verticalDist + perihelionDist
yValue = constY + (verticalDist / 2 - ORBIT_OBJECT_RADIUS - perihelionDist)

# Create figure and axes
fig, ax = plt.subplots()

# Define ellipse: center (x, y), width, height, angle in degrees
ellipse = Ellipse(
    xy=(CONST_X, yValue), width=verticalDist, height=verticalDist * WIDTH_TO_HEIGHT_RATIO, angle=90, edgecolor='gray', facecolor='white'
)
ax.add_patch(ellipse)

# 2. Add the Circle: center (x, y), radius
orbitAround = plt.Circle(
    xy=(CONST_X, constY), radius=ORBIT_OBJECT_RADIUS, edgecolor='lightblue', facecolor='lightblue', label='Orbit around'
)
ax.add_patch(orbitAround)

# Semi-axes lengths
a = verticalDist / 2  # Semi-vertical axis
b = (verticalDist * WIDTH_TO_HEIGHT_RATIO) / 2  # Semi-horizontal axis

# Configure axes
ax.set_xlim(0, CONST_X * 2)
ax.set_ylim(0, maxY)
ax.set_aspect('equal')
ax.set_title('Asteroid orbit')
ax.axis('off')
# Display in Streamlit
st.pyplot(fig)
