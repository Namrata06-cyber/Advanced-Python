
import pandas as pd
import matplotlib.pyplot as plt

# 1. Create employee DataFrame
data = {
    'Name': ['Amit', 'Riya', 'Rahul', 'Priya', 'Sneha',
             'Karan', 'Neha', 'Rohan', 'Pooja', 'Arjun'],
    'Age': [24, 25, 28, 23, 26, 30, 27, 29, 24, 35],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'Marketing',
                   'Finance', 'HR', 'IT', 'Marketing', 'IT'],
    'Salary': [30000, 35000, 40000, 32000, 38000,
               45000, 36000, 42000, 39000, 200000]
}

df = pd.DataFrame(data)

print("Original Employee Data:")
print(df)

# 2. Calculate salary statistics
print("\nSalary Statistics")
print("Mean:", df['Salary'].mean())
print("Median:", df['Salary'].median())
print("Standard Deviation:", df['Salary'].std())

# 3. Calculate IQR and detect outliers
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("\nLower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

outliers = df[
    (df['Salary'] < lower_limit) |
    (df['Salary'] > upper_limit)
]

print("\nDetected Outliers:")
print(outliers)

# 4. Remove outliers
clean_df = df[
    (df['Salary'] >= lower_limit) &
    (df['Salary'] <= upper_limit)
]

print("\nData After Removing Outliers:")
print(clean_df)

# 5. Plot boxplot and histogram
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.boxplot(df['Salary'])
plt.title("Salary Boxplot")
plt.ylabel("Salary")

plt.subplot(1, 2, 2)
plt.hist(df['Salary'], bins=6, edgecolor='black')
plt.title("Salary Histogram")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()