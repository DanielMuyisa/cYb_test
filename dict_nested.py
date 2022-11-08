mb = {
    "first": {
        'id': 1,
        'name': 'username',
        'age': 20,
    },
    "second": {
        'id': 2,
        'name': 'name 2',
        'age': 30,
    }
}


for i in mb:
    for j in mb[i]:
        print(mb[i].get("name"))
