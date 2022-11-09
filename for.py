# print befor
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

# print after
print("--------------")
for x in fruits:
    print(x)
    if x == "banana":
        break

# escape a item
print("--------------")
for x in fruits:
    if x == 'banana':
        continue
    print(x)

# range
# for x in range(10):
print("--------------")
for x in range(0, 10):
    print(x)

# range increment sequence
print("--------------")
for i in range(0, 10, 3):
    print(i)

# nested for
print("------- nested-------")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

# for pass
print('-----------------')
for x in [0, 1, 2]:
    pass
    print(x)
