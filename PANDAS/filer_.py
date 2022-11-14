import pandas as pd

path = "./manage/files/csv/electronic.csv"
df = pd.read_csv(path)

# print(df.head(1))
# print(df.info())

# replace empty spaces a value
# df.fillna("---- pas de valuer ---", inplace=True)

# replace in a specifique field

df['Series_reference'].fillna("--------", inplace=True)

print(df)
