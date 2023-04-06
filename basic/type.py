n = 10
# complex
t = 3+5j
print(type(n))
print(type(t))
print(str(n))

# convert complex  to int
c = complex(n)
print(type(c))

# bytes
bt = bytes(5)
print(bt)
print(bytearray(5))

# memoryview
memo = memoryview(bytes(5))
print(memo)
