import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load & clean data
df = pd.read_csv("metadata.csv")
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research metadata (titles, journals, dates).")

# Year filter
year_range = st.slider("Select year range", 2018, 2023, (2020, 2021))
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.write(f"### Number of papers in selected range: {len(filtered)}")

# Visualization: publications by year
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax)
plt.title("Publications by Year")
st.pyplot(fig)

# Top journals
top_journals = filtered['journal'].value_counts().head(10)
st.write("### Top Journals")
st.bar_chart(top_journals)

# Show data sample
st.write("### Sample Data")
st.dataframe(filtered[['title', 'journal', 'publish_time']].head(20))
