# like a table with arrays and columns

import pandas as pd

data = {
    "one": [1, 2, 3],
    "two": ['a', 'b', 'c', ]
}

rs = pd.DataFrame(data)
print(rs)

# locate row
print(rs.loc[[1, 2]])

# name rows
print("------")
rs = pd.DataFrame(data, index=["row0", "row1", "row2"])
print(rs.loc[["row0", "row2"]])
