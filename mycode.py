import pandas as pd
import numpy as np
import os

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [24, 30, 22, 35],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)

new_row = pd.DataFrame({'Name': ['Eve'],
                      'Age': [28],
                      'City': ['Seattle']})
df = pd.concat([df, new_row], ignore_index=True)

new_row = pd.DataFrame({'Name': ['Frank'],
                      'Age': [29],
                      'City': ['Miami']})
df = pd.concat([df, new_row], ignore_index=True)

print("Original DataFrame:")
print(df)

data_dir = 'data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

file_path = os.path.join(data_dir, 'data.csv')

df.to_csv(file_path, index=False)
print(f"\nDataFrame saved to {file_path}")