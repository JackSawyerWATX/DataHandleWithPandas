import pandas as pd

data = {'age': [25, 30, 35], 'salary': [50000, 60000, 80000]}
df = pd.DataFrame(data)

print(df.describe())
print(df.isnull().sum())
