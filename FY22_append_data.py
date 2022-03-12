import os
import pandas as pd

file_list = [file for file in os.listdir('FY2022_485/') if file.endswith('.csv')]
print(file_list)

df = pd.read_csv('FY2022/CaseNum-all_status.csv')
for file in file_list:
    df_temp = pd.read_csv(f'FY2022_485/{file}')
    df = pd.concat([df, df_temp], ignore_index=True)

df = df.sort_values(by=['CaseNum', 'Status_Short', 'Generated_at'])
print(df.shape)

df = df.drop_duplicates(subset=['CaseNum', 'Date'], keep='first')
print(df.shape)

df.to_csv('FY2022/CaseNum-all_status.csv', index=False)
