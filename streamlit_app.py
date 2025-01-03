import streamlit as st

st.title("Live Plots with Persistent Links")

# Persistent OneDrive public links
plot_urls = [
    "https://raw.githubusercontent.com/krishangguptafibonacciresearch/distro_project/main/ZN_1m_Volatility_Distribution_2024-09-30_2024-12-26_High_Low_.png"
]

st.header("Generated Plots")
for url in plot_urls:
    st.image(url, caption="Plot from OneDrive")
