import streamlit as st

st.title("Live Plots with Persistent Links @ FR")

# Persistent OneDrive public links
plot_urls = [
    "https://raw.githubusercontent.com/krishangguptafibonacciresearch/distro_project/main/Intraday_data_files_stats_and_plots_folder/ZN_15m_Returns_Distribution_2024-11-03_2025-01-06.png",
    "https://raw.githubusercontent.com/krishangguptafibonacciresearch/distro_project/main/Intraday_data_files_stats_and_plots_folder/ZN_15m_Volatility_Distribution_2024-11-03_2025-01-06_High_Low_.png",
    "https://raw.githubusercontent.com/krishangguptafibonacciresearch/distro_project/main/Intraday_data_files_stats_and_plots_folder/ZN_1h_Returns_Distribution_2022-12-20_2025-01-05.png",
    "https://raw.githubusercontent.com/krishangguptafibonacciresearch/distro_project/main/Intraday_data_files_stats_and_plots_folder/ZN_1h_Volatility_Distribution_2022-12-20_2025-01-05_High_Low_.png",
    "https://raw.githubusercontent.com/krishangguptafibonacciresearch/distro_project/main/Intraday_data_files_stats_and_plots_folder/ZN_1m_Returns_Distribution_2024-09-30_2025-01-06.png",
    "https://raw.githubusercontent.com/krishangguptafibonacciresearch/distro_project/main/Intraday_data_files_stats_and_plots_folder/ZN_1m_Volatility_Distribution_2024-09-30_2025-01-06_High_Low_.png",
]

x = st.sidebar.selectbox("Select Duration",["1 min" , "15 min" , "1 hr"])

st.header("Generated Plots")
if x == "15 min":
    st.image(plot_urls[0] , caption = "Returns Distribution")
    st.image(plot_urls[1] , caption = "Volatility Distribution")
elif x == "1 hr":
    st.image(plot_urls[2] , caption = "Returns Distribution")
    st.image(plot_urls[3] , caption = "Volatility Distribution")
else:
    st.image(plot_urls[4] , caption = "Returns Distribution")
    st.image(plot_urls[5] , caption = "Volatility Distribution")
