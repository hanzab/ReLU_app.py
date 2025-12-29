import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("ReLU Activation Function")
x = np.linspace(-10,10,100)
y = np.maximum(0,x)
fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)
