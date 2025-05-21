import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define Base URL for GitHub-hosted datasets
BASE_URL = "https://raw.githubusercontent.com/codebeki/solar-challenge-week1/refs/heads/dashboard-dev/data/"

#  List of datasets to load dynamically
DATASETS = {
    "Benin-Malanville": "benin-malanville.csv",
    "Sierra Leone": "sierraleone-bumbuna.csv",
    "Togo": "togo-dapaong_qc.csv"
}

#  Load datasets from GitHub dynamically
@st.cache_data
def load_data():
    """
    Fetch datasets dynamically from GitHub-hosted CSV files.

    Returns:
    dict: Dictionary containing dataframes of each country.
    """
    data = {}
    for country, filename in DATASETS.items():
        try:
            data[country] = pd.read_csv(BASE_URL + filename)
        except Exception as e:
            st.error(f"Error loading {country} dataset: {e}")
    
    return data

data = load_data()

#  App Title
st.title("Solar Energy Analysis Dashboard 🌞")

#  Country Selection Dropdown
if data:
    selected_country = st.selectbox("Select a country", options=list(data.keys()))
    df = data[selected_country]
    st.write(f"Showing data for: {selected_country}")

    #  Boxplot for GHI
    st.subheader("Solar Irradiance Boxplot (GHI)")
    fig, ax = plt.subplots()
    sns.boxplot(y=df["GHI"], ax=ax)
    st.pyplot(fig)

    #  Summary Table
    st.subheader("Summary Statistics")
    st.write(df[["GHI", "DNI", "DHI"]].describe())

    #  Rank Countries by Avg GHI
    ghi_avg = {country: df["GHI"].mean() for country, df in data.items()}
    sorted_ghi = pd.DataFrame(ghi_avg.items(), columns=["Country", "Avg GHI"]).sort_values(by="Avg GHI", ascending=False)
    st.subheader("Top Regions by Solar Potential")
    st.table(sorted_ghi)

else:
    st.error("Data could not be loaded. Please check file availability.")
