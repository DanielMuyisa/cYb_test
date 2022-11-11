import re

synt = 'All people seems to need data processing'
synt2 = "Hey con, i'm looking the the hacker-one forum"
# search = re.search("^All.*processing$", synt)


# print(search)

# print a list of all matches
res = re.findall('data', synt)

print(res)

# split all white-space
wt = re.split("\s", synt)
print(wt)

# replate every white space substr
rp = re.sub("\s", "---", synt)
print(rp)

# print the word where there wos a match
match = re.search(r"\bs\w+", synt)
res_of_match = match.group()
# print(res_of_match)


# print the word contains hacker
hk = re.search(r"\bh\w+", synt2)
res_hk = hk.group()
print(res_hk)
