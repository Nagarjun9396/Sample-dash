import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data
np.random.seed(42)
data = {
    'Date': pd.date_range(start='2024-01-01', periods=100),
    'Sales': np.random.randint(100, 500, size=100),
    'Location': np.random.choice(['North', 'South', 'East', 'West'], size=100)
}
df = pd.DataFrame(data)

st.title('Interactive Sales Dashboard By Nagarjuna')

# Sidebar for user input
st.sidebar.header('User Input')

locations = df['Location'].unique()
selected_location = st.sidebar.selectbox('Select Location', locations)

# Filter data based on user input
filtered_df = df[df['Location'] == selected_location]

# Display data
st.subheader(f'Sales Data for {selected_location}')
st.write(filtered_df)

# Plotting
st.subheader('Sales Trend')
fig, ax = plt.subplots()
ax.plot(filtered_df['Date'], filtered_df['Sales'], marker='o', linestyle='-')
ax.set_xlabel('Date')
ax.set_ylabel('Sales')
ax.set_title(f'Sales Trend for {selected_location}')
st.pyplot(fig)

# Display statistics
st.subheader('Statistics')
st.write(f"**Total Sales**: {filtered_df['Sales'].sum()}")
st.write(f"**Average Sales**: {filtered_df['Sales'].mean()}")
st.write(f"**Maximum Sales**: {filtered_df['Sales'].max()}")
st.write(f"**Minimum Sales**: {filtered_df['Sales'].min()}")
