mb = {
    'id': 1,
    'name': 'username',
    'age': 20,
}

#
for i in mb:
    print(i)

# vals
for i in mb.keys():
    print(mb[i])

# items - key|valeur
for x, y in mb.items():
    print(x, y)

members = {}
members.update({
    "name": 'username',
    'age': 20
})

turn = 0
for x, y in members.items():
    if turn <= 1:
        turn += 1
        print(x, y)
