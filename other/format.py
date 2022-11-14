snt = "I'm live my life like every day is {}"

lst = ["Monday", "Tuesday", "wednezday",
       "Truday", "friday", "Saturday", "sunday"]

i = 0
while (i < len(lst)):
    print(snt.format(lst[i]))
    i += 1


# i = 0
# while i in range(len(lst)):
#     frmt = snt.format(lst[i])
#     print(frmt)
#     i += 1


# indexed paman
x = 2
y = 3
z = 4
sx = "number {2} and number {0} were registered in class {1}"
res = sx.format(x, y, z)
print(res)


# named index
st = "we are {w}, we can {n}, coz we're {s}"
rs = st.format(w="world", n="win", s="strong")
print(rs)
