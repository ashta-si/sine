
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(layout="wide")
st.title("🎵 Sine Wave Visualizer (Live Update)")

# Sliders
amp = st.slider("Amplitude", 0.0, 10.0, 1.0, 0.1)
freq = st.slider("Frequency", 0.1, 10.0, 1.0, 0.1)
speed = st.slider("Phase Speed", 0.0, 1.0, 0.1, 0.01)

# Animation checkbox
animate = st.checkbox("Animate", value=True)

# Plot container
plot_area = st.empty()

# X-axis
x = np.linspace(0, 2 * np.pi, 1000)

# Loop
frame = 0
while animate:
    phase = frame * speed
    y = amp * np.sin(freq * x + phase)

    fig, ax = plt.subplots()
    ax.plot(x, y, color='cyan')
    ax.set_ylim(-10, 10)
    ax.set_title("Sine Wave")
    ax.grid(True)

    plot_area.pyplot(fig)
    plt.close(fig)

    time.sleep(0.05)
    frame += 1
