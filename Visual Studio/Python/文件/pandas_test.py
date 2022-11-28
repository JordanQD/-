import os
import pandas as pd
path = '/Users/jordan_qd/Desktop/51st Bisons vs CNF Rd 1__10HZ'
filename = '51st Bisons vs CNF Rd 1__10HZ.csv'
file = os.path.join(path,filename)

df = pd.read_csv(file)
print('dataframe:')
print(df)

df1 = df.iloc[df['Type']=='Air+FixedWing:,']
df2 = df.loc[:,df['Type'=='Air+FixedWing']]
print(df2)