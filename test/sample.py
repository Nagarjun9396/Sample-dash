import pandas as pd
import time

# Start the timer
start_time = time.time()

# Load the Excel file
file_path = "C:\\Users\\nagar\\Downloads\\samp.xlsx"  # Replace with your file path
raw_df = pd.read_excel(file_path)

# Display the first few rows of the dataframe
# print(raw_df.head())

df = raw_df.groupby('City').size().reset_index(name='Count')

print(df)



# Stop the timer and calculate the elapsed time
end_time = time.time()
elapsed_time = end_time - start_time

# Print the time taken
print(f"Time taken to execute the code: {elapsed_time:.2f} seconds")