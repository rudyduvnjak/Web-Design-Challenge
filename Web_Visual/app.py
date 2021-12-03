import pandas as pd

# Convert csv file into data frame
df_cities = pd.read_csv('Resources/cities.csv')

# 
df_cities.to_html('data_table.html', index=False)

# Create html table
table = df_cities.to_html()
print(table)