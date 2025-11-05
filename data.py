import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Create more complex sample data
np.random.seed(42)  # For reproducible results

# Generate employee data
n_employees = 100
data = {
    'employee_id': range(1, n_employees + 1),
    'name': [f'Employee_{i}' for i in range(1, n_employees + 1)],
    'age': np.random.normal(35, 8, n_employees).astype(int),
    'salary': np.random.normal(65000, 15000, n_employees).round(2),
    'department': np.random.choice(['IT', 'HR', 'Finance', 'Marketing', 'Operations'], n_employees),
    'years_experience': np.random.exponential(5, n_employees).round(1),
    'performance_score': np.random.uniform(1, 5, n_employees).round(2),
    'hire_date': [datetime(2020, 1, 1) + timedelta(days=int(x)) for x in np.random.randint(0, 1460, n_employees)],
    'is_remote': np.random.choice([True, False], n_employees, p=[0.3, 0.7])
}

# Add some missing values to make it realistic
missing_indices = np.random.choice(n_employees, size=int(n_employees * 0.05), replace=False)
for idx in missing_indices:
    data['performance_score'][idx] = np.nan

df = pd.DataFrame(data)

# Ensure age is within realistic bounds
df['age'] = df['age'].clip(22, 65)

print("=== BASIC DATA OVERVIEW ===")
print(f"Dataset shape: {df.shape}")
print(f"Data types:\n{df.dtypes}\n")

print("=== STATISTICAL SUMMARY ===")
print(df.describe())
print()

print("=== MISSING VALUES ANALYSIS ===")
missing_data = df.isnull().sum()
print(f"Missing values per column:\n{missing_data[missing_data > 0]}")
print(f"Total missing values: {df.isnull().sum().sum()}")
print()

print("=== DEPARTMENT ANALYSIS ===")
dept_stats = df.groupby('department').agg({
    'salary': ['mean', 'median', 'count'],
    'age': 'mean',
    'years_experience': 'mean',
    'performance_score': 'mean'
}).round(2)
print(dept_stats)
print()

print("=== CORRELATION ANALYSIS ===")
numeric_cols = ['age', 'salary', 'years_experience', 'performance_score']
correlation_matrix = df[numeric_cols].corr()
print(correlation_matrix.round(3))
print()

print("=== SALARY ANALYSIS BY DEPARTMENT ===")
salary_by_dept = df.groupby('department')['salary'].agg(['count', 'mean', 'std', 'min', 'max']).round(2)
print(salary_by_dept)
print()

print("=== HIGH PERFORMERS (Score > 4.0) ===")
high_performers = df[df['performance_score'] > 4.0]
print(f"Number of high performers: {len(high_performers)}")
print(f"Average salary of high performers: ${high_performers['salary'].mean():.2f}")
print(f"Department distribution of high performers:")
print(high_performers['department'].value_counts())
print()

print("=== REMOTE WORK ANALYSIS ===")
remote_stats = df.groupby('is_remote').agg({
    'salary': 'mean',
    'performance_score': 'mean',
    'years_experience': 'mean'
}).round(2)
remote_stats.index = ['In-Office', 'Remote']
print(remote_stats)
print()

print("=== DATA FILTERING EXAMPLES ===")
# Senior employees (5+ years experience) in IT department
senior_it = df[(df['years_experience'] >= 5) & (df['department'] == 'IT')]
print(f"Senior IT employees: {len(senior_it)}")

# High salary employees (top 10%)
salary_threshold = df['salary'].quantile(0.9)
high_earners = df[df['salary'] >= salary_threshold]
print(f"Top 10% earners (${salary_threshold:.2f}+): {len(high_earners)} employees")

# Recent hires (hired in last year)
recent_hire_date = datetime.now() - timedelta(days=365)
recent_hires = df[df['hire_date'] >= recent_hire_date]
print(f"Recent hires (last year): {len(recent_hires)} employees")
print()

print("=== CUSTOM METRICS ===")
# Create salary bands
df['salary_band'] = pd.cut(df['salary'], 
                          bins=[0, 50000, 70000, 90000, float('inf')], 
                          labels=['Low', 'Medium', 'High', 'Very High'])

print("Salary band distribution:")
print(df['salary_band'].value_counts())
print()

# Calculate tenure in years
df['tenure_years'] = (datetime.now() - df['hire_date']).dt.days / 365.25

print("=== ADVANCED AGGREGATIONS ===")
# Multi-level grouping
advanced_grouping = df.groupby(['department', 'is_remote']).agg({
    'salary': ['mean', 'count'],
    'performance_score': 'mean'
}).round(2)
print("Department & Remote work breakdown:")
print(advanced_grouping)
print()

# Handle missing values
print("=== DATA CLEANING ===")
print(f"Before cleaning - Performance score nulls: {df['performance_score'].isnull().sum()}")

# Fill missing performance scores with department median
df['performance_score'] = df.groupby('department')['performance_score'].transform(
    lambda x: x.fillna(x.median())
)

print(f"After cleaning - Performance score nulls: {df['performance_score'].isnull().sum()}")
print()

print("=== EXPORT SUMMARY ===")
# Save processed data
df.to_csv('employee_data_processed.csv', index=False)
print("✓ Data saved to 'employee_data_processed.csv'")

# Save department summary
dept_summary = df.groupby('department').agg({
    'salary': ['mean', 'median', 'std'],
    'performance_score': 'mean',
    'employee_id': 'count'
}).round(2)
dept_summary.to_csv('department_summary.csv')
print("✓ Department summary saved to 'department_summary.csv'")

print("\n=== ANALYSIS COMPLETE ===")
print(f"Processed {len(df)} employee records across {df['department'].nunique()} departments")
