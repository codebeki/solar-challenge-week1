import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned datasets
@st.cache_data
def load_data():
    benin = pd.read_csv("data/benin_clean.csv")
    sierra_leone = pd.read_csv("data/sierraleone_clean.csv")
    togo = pd.read_csv("data/togo_clean.csv")
    return {"Benin": benin, "Sierra Leone": sierra_leone, "Togo": togo}

data = load_data()

# App Title
st.title("Solar Energy Analysis Dashboard 🌞")

# Country Selection
selected_country = st.selectbox("Select a country", options=list(data.keys()))
df = data[selected_country]
st.write(f"Showing data for: {selected_country}")

# Boxplot for GHI
st.subheader("Solar Irradiance Boxplot (GHI)")
fig, ax = plt.subplots()
sns.boxplot(y=df["GHI"], ax=ax)
st.pyplot(fig)

# Summary Table
st.subheader("Summary Statistics")
st.write(df[["GHI", "DNI", "DHI"]].describe())

# Rank Countries by Avg GHI
ghi_avg = {country: df["GHI"].mean() for country, df in data.items()}
sorted_ghi = pd.DataFrame(ghi_avg.items(), columns=["Country", "Avg GHI"]).sort_values(by="Avg GHI", ascending=False)
st.subheader("Top Regions by Solar Potential")
st.table(sorted_ghi)
