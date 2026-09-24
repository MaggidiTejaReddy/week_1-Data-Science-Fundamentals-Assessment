# Part 4: Basic Data Analysis

import pandas as pd
import matplotlib.pyplot as plt

# Create dataset
data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Age": [20, 21, 19, 20, 22],
    "Python_Marks": [85, 78, 92, 88, 76],
    "Statistics_Marks": [80, 75, 90, 85, 70]
}

df = pd.DataFrame(data)

print("DATASET")
print("-" * 40)

print(df)

# Basic information
print("\nDataset Information:")
print(df.info())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Average marks
print("\nAverage Python Marks:",
      df["Python_Marks"].mean())

print("Average Statistics Marks:",
      df["Statistics_Marks"].mean())

# Highest Python marks
print("\nHighest Python Marks:",
      df["Python_Marks"].max())

# Student with highest Python marks
highest_student = df.loc[df["Python_Marks"].idxmax(), "Name"]

print("Student with highest Python marks:",
      highest_student)

# Visualization
plt.bar(df["Name"], df["Python_Marks"])

plt.xlabel("Students")
plt.ylabel("Python Marks")
plt.title("Python Marks of Students")

plt.show()