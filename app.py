import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Set layout
st.set_page_config(layout="wide")
st.title("🎵 Sine Wave Visualizer (Live Update)")

# Sliders
amp = st.slider("Amplitude", 0.0, 10.0, 1.0, 0.1)
freq = st.slider("Frequency", 0.1, 10.0, 1.0, 0.1)
speed = st.slider("Phase Speed", 0.0, 1.0, 0.1, 0.01)

# Animate toggle
animate = st.checkbox("Animate", value=True)

# Plot placeholder
plot_area = st.empty()

# X-axis
x = np.linspace(0, 2 * np.pi, 1000)

# Frame counter
frame = 0

# ✅ Main loop with safety
while animate and frame < 200:  # Limit frames to prevent freezing
    phase = frame * speed
    y = amp * np.sin(freq * x + phase)

    fig, ax = plt.subplots()
    ax.plot(x, y, color='cyan')
    ax.set_ylim(-10, 10)
    ax.set_title("Sine Wave")
    ax.grid(True)

    plot_area.pyplot(fig)
    plt.close(fig)

    time.sleep(0.1)  # ⬅️ Reduce CPU usage
    frame += 1
