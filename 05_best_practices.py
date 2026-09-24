# Part 5: Data Science Best Practices

import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Age": [20, 21, None, 20, 22],
    "Marks": [85, 78, 92, None, 76]
}

df = pd.DataFrame(data)

print("ORIGINAL DATA")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nDATA AFTER HANDLING MISSING VALUES")
print(df)

# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()

print("\nFINAL DATASET")
print(df)