import pandas as pd
import numpy as np

# Create a data set
data = {
    'Student_ID': [1001, 1002, 1003, 1004, 1005],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Marks': [85, 92, np.nan, 88, 76], # Missing value
    'Study_Hours': [4, 9, 2, 1, 3]
}

# Load into a DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Analyze the DataFrame
print("\nStatistical Summary:")
print(df.describe())

# Cleaning data
print("\nFilling missing values in 'Marks' with the mean:")

# Calculate the mean of 'Marks' column
avg_mark = df['Marks'].mean()
print(f"Average Marks: {avg_mark}")

# Fill NaN values with the average
df['Marks'] = df['Marks'].fillna(avg_mark)

print("\nDataFrame after filling missing values:")
print(df)

# Filtering data: Students who scored more than 50 marks
print("\nStudents who scored more than 50 marks:")
passed_students = df[df['Marks'] > 50]
print(passed_students[['Name', 'Marks']])

# Saving cleaned data to a new CSV file
df.to_csv('cleaned_student_data.csv', index=False)
print("\nCleaned data saved to 'cleaned_student_data.csv'")