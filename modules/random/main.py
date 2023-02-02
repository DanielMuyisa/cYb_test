import random

# x = random.uniform(2, 6)
x = random.randint(1, 106)
print(x)


# choix aleatoire dans une liste
lst = ("php", "java", "linux", "windows", "Mac")
alChoice = random.choice(lst)
print(alChoice)

# try to devine 5 number from 0 to 100
print("------------")
debut = 0
limit = 5
table = []
# for x in range(5):
for i in range(0, 100):
    table.append(i)
    if len(table) >= 100:
        for j in table:

            if debut < 5:
                print(random.choice(table))
                debut += 1
    # print("------------------------------------")
