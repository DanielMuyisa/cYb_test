mb = {
    'id': 1,
    'name': 'username',
    'age': 20,
}

# get
x = mb.get('id')
# print(x)

# keys
keys = mb.keys()
# print(keys)

# chenge value
mb['id'] = 2
# print(mb.values())

# update dict
mb.update({
    'name': "root",
    'age': 0,
})

# print(mb.values())


# add value
mb['genre'] = 'X'
# print(mb)

# copy dict
new_dict = mb.copy()
new_dict.update({
    'name': 'new name',
    'age': 40
})
# print(new_dict)

# copy with dict fx
dict_fx = dict(new_dict)
print(dict_fx.keys())
