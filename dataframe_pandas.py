import pandas as pd

# Create a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [24, 27, 22]}

df = pd.DataFrame(data)

print(df)

# Detect missing values
print(df.isnull())

# Drop rows with missing values
print(df.dropna())

# Fill missing values
print(df.fillna({'Age': df['Age'].mean()}))