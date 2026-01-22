# PANDAS 
# If data is dirty -> model will fail silently
# Data cleaning is the most important part of data science

# DATA FRAME = EXCEL SHEET = TABLE
# Series = COLUMN
# Index = Row number (0,1,2,...)

# pandas always thinks in columns (series)

# NaN = Not a Number = missing value
# Why is it dangerous?
# 1. If you have NaN in your data, many algorithms will fail

# Creating a DataFrame - a 2d labeled data structure optimized for column-wise operations
# df = pd.DataFrame(data)

# Always inspect your data after loading it
# df.head()  # first 5 rows
# print(df) - prints entire dataframe
# df.info() - summary of dataframe
# df.describe() - statistical summary of numerical columns
# df.columns - list of column names
# df.shape - (num_rows, num_columns)
# df.dtypes - data types of each column

# Cleaning Data
# Missing values with class average
# df['column_name'] = df['column_name'].fillna(df['column_name'].mean()

# Find NaN -> Decide strategy -> Replace

# FILTERING DATA
# df_filtered = df[df['column_name'] > value]
# Boolean masking
# No loops, no if statements, pure vectorized speed

# COLUMN SELECTION - DATA SHAPE MATTERS
# DataFrame = 2D table ex [[Marks]] = 85, 90, 78, ...
# passed_students[['name', 'score']]  # double brackets to keep it as DataFrame (table)
# Series = 1D [85, 90, 78, ...]
# passed_students['name']  # single brackets returns Series (column)

# SAVING DATA
# df.to_csv('cleaned_data.csv', index=False)
# index=False to avoid saving the index as a separate column

# REAL ML PIPELINE

# Raw Data -> Pandas Cleaning -> Clean CSV -> Feature Engineering -> Model Training