import streamlit as st
import os

st.set_page_config(
    page_title="FR Live Plots",
    page_icon="FR",
    layout="wide",
    initial_sidebar_state="expanded",
)

repo_name='distro_project'
branch='main'
st.title("Live Plots with Persistent Links @ FR")

plots_directory="delete"#"Intraday_data_files_stats_and_plots_folder"
plot_url_base=f"https://raw.githubusercontent.com/krishangguptafibonacciresearch/{repo_name}/{branch}/{plots_directory}/"

plot_urls=[]
intervals=[]
instruments=[]
return_types=[]
for plotfile in os.scandir(plots_directory):
    if plotfile.is_file() and plotfile.name.endswith('.png'):
        plotfile_content=plotfile.name.split('_')
        plot_url=plot_url_base+plotfile.name
        instrument=plotfile_content[0]
        interval=plotfile_content[1]
        return_type=plotfile_content[2]

        intervals.append(interval)
        instruments.append(instrument)
        plot_urls.append({
            "url": plot_url,
            "instrument": instrument,
            "interval": interval,
            "return_type": return_type
        })

# Persistent OneDrive public links
# plot_urls = [
#     "https://raw.githubusercontent.com/krishangguptafibonacciresearch/distro_project/main/Intraday_data_files_stats_and_plots_folder/ZN_15m_Returns_Distribution.png",
#     "https://raw.githubusercontent.com/krishangguptafibonacciresearch/distro_project/main/Intraday_data_files_stats_and_plots_folder/ZN_15m_Volatility_Distribution.png",
#     "https://raw.githubusercontent.com/krishangguptafibonacciresearch/distro_project/main/Intraday_data_files_stats_and_plots_folder/ZN_1h_Returns_Distribution.png",
#     "https://raw.githubusercontent.com/krishangguptafibonacciresearch/distro_project/main/Intraday_data_files_stats_and_plots_folder/ZN_1h_Volatility_Distribution.png",
#     "https://raw.githubusercontent.com/krishangguptafibonacciresearch/distro_project/main/Intraday_data_files_stats_and_plots_folder/ZN_1m_Returns_Distribution.png",
#     "https://raw.githubusercontent.com/krishangguptafibonacciresearch/distro_project/main/Intraday_data_files_stats_and_plots_folder/ZN_1m_Volatility_Distribution.png",
# ]

unique_intervals=set(intervals)
unique_instruments=set(instruments)
#st.sidebar.title("Settings")
#st.sidebar.markdown("Use the selectors below to filter plots.")
#st.sidebar.help("Select your preferred interval and instrument to view the corresponding plots.")

x = st.sidebar.selectbox("Select Interval",unique_intervals)
y= st.sidebar.selectbox("Select Instrument",unique_instruments)
st.header("Generated Plots")
#st.image(plot_urls[0] , caption = "Returns Distribution")
filtered_plots = [plot for plot in plot_urls if plot["interval"] == x and plot["instrument"] == y]
st.write('https://raw.githubusercontent.com/krishangguptafibonacciresearch/distro_project/main/delete/ZN_1h_Returns_Distribution.png')
#st.header("Generated Plots")
# Display plots
if filtered_plots:
    for plot in filtered_plots:
        caption = f"{plot['return_type'].replace('Returns', 'Returns Distribution').replace('Volatility', 'Volatility Distribution')}"
        st.write(plot['url'])
        st.image(plot['url'],caption=caption)
    #     st.download_button(
    #     label="Download Plot",
    #     data=plot["url"],
    #     file_name=f"{plot['instrument']}_{plot['interval']}.png",
    #     mime="image/png"
    # )
else:
    st.write("No plots found for the selected interval and instrument.")
