import pandas as pd

a = [1, 2, 3]
rs = pd.Series(a, index=["x", "y", "z"])

print(rs)
print(rs['x'])

# key/value
print("------------")
net = {
    "router": 10,
    "switchs": 20,
    "topology": 'annau',
}
rs = pd.Series(net)

# select
rs = pd.Series(net, index=["router"])
print(rs)

# ***** DATA FRAME
print("------------")
data = {
    "one": [1, 2, 3, 4, 5, 6],
    "two": ['a', 'b', 'c', 'd', 'e', 'f']
}

rs = pd.Series(data)
print(rs)
