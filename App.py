import streamlit as st
import pandas as pd


st.set_page_config( page_title = "Dashboard", page_icon = '📶' )

# Sample DataFrame
data = {
    'Sales Rep': ['Alice', 'Bob', 'Charlie', 'David', 'Edward'],
    'Location': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Sales': [1500, 2000, 1700, 1200, 2300]
}

df = pd.DataFrame(data)

# Sidebar filters
st.sidebar.header('Filter options')

# Collapsible Sales Rep Filter
with st.sidebar.expander('Sales Rep', expanded=False):
    all_sales_reps = df['Sales Rep'].unique().tolist()
    selected_sales_reps = []
    select_all_sales_reps = st.checkbox('Select All Sales Reps', value=True)

    if select_all_sales_reps:
        selected_sales_reps = all_sales_reps
    else:
        for sales_rep in all_sales_reps:
            if st.checkbox(sales_rep, value=False):
                selected_sales_reps.append(sales_rep)

# Collapsible Location Filter
with st.sidebar.expander('Location', expanded=False):
    all_locations = df['Location'].unique().tolist()
    selected_locations = []
    select_all_locations = st.checkbox('Select All Locations', value=True)

    if select_all_locations:
        selected_locations = all_locations
    else:
        for location in all_locations:
            if st.checkbox(location, value=False):
                selected_locations.append(location)

use_slider = st.sidebar.checkbox('Use Sales Range Slider')

if use_slider:
    sales_range = st.sidebar.slider(
        'Select Sales Range:',
        min_value=int(df['Sales'].min()),
        max_value=int(df['Sales'].max()),
        value=(int(df['Sales'].min()), int(df['Sales'].max()))
    )
    min_sales, max_sales = sales_range
else:
    # Number inputs for manual min and max values
    min_sales = st.sidebar.number_input(
        'Enter Minimum Sales:',
        min_value=int(df['Sales'].min()),
        max_value=int(df['Sales'].max()),
        value=int(df['Sales'].min())
    )

    max_sales = st.sidebar.number_input(
        'Enter Maximum Sales:',
        min_value=int(df['Sales'].min()),
        max_value=int(df['Sales'].max()),
        value=int(df['Sales'].max())
    )

# Ensure that the min_sales is always less than or equal to max_sales
if min_sales > max_sales:
    st.sidebar.error("Minimum sales cannot be greater than maximum sales.")



# Apply filters to the DataFrame
filtered_df = df[
    (df['Sales Rep'].isin(selected_sales_reps)) &
    (df['Location'].isin(selected_locations)) &
    (df['Sales'].between(min_sales,max_sales))
]

# Display filtered DataFrame
with st.expander('Data', expanded= True):
  st.write("### Filtered Data", filtered_df)
