# Q1
import pandas as pd
df=pd.read_csv("patient_details.csv")
print ("Patient Details Dataset:")
print(df)
print(df.ndim)
print(df.shape)
print(df.size)
print(df.head(5))
print(df.describe())
print("\nChecking for missing values:")
print(df.isnull())
print(df.isnull().sum())

df['name'].fillna('Unknown', inplace=True)
print(df)

print(df.isnull().sum())
df['age'].fillna(df['age'].mean(), inplace=True)
print(df)
print(df.isnull().sum())



# Q2
import pandas as pd
df=pd.read_csv("medical_records.csv")
print ("Medical Details Dataset:")
print(df)
print(df.isnull().sum())
df['sugar_level'].fillna('0', inplace=True)
print(df)

#0 because many don't have sugar level records
