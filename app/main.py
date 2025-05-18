import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data (Ensure data/ is ignored)
@st.cache_data
def load_data():
    return {
        "Benin": pd.DataFrame(),  # Placeholder without actual data
        "Sierra Leone": pd.DataFrame(),
        "Togo": pd.DataFrame(),
    }

data = load_data()

# UI Setup
st.title("Solar Energy Analysis Dashboard 🌞")
selected_country = st.selectbox("Select a country", options=list(data.keys()))
df = data[selected_country]

# Visualization: Example Boxplot
st.subheader("Solar Irradiance Boxplot")
fig, ax = plt.subplots()
sns.boxplot(y=df.get("GHI", pd.Series()), ax=ax)
st.pyplot(fig)

# Summary Table
st.subheader("Summary Statistics")
st.write(df.describe())
