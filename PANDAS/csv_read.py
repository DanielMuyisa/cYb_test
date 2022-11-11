import pandas as pd

path = "./manage/files/csv/electronic.csv"
file = pd.read_csv(path)

# max row to read
max = pd.options.display.max_rows
print(max)

# specify the max rows/column to print
pd.options.display.max_columns = 2
pd.options.display.max_rows = 2
rs = pd.read_csv(path)
print(rs)
