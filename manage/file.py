import os
new = open("./manage/files/newfile.txt", "a")
txt = ""
for i in range(20):
    txt += "This is a new line \n"

new.write(txt)
new.close


# "w" create new file if not exists
# "x" return error if file exists

s = open("./manage/files/n.txt", "w")
rs = s.write("hello world")
s.close()


# read
# open
open = open("./manage/files/newfile.txt", "r")
# print(open.read())
# print(open.read(5))
print(open.readline())
open.close()

# delete file
try:
    if os.path.exists("./manage/files/n.txt"):
        rs = os.remove("./manage/files/n.txt")
        print("file havebeen removed")
except NameError:
    print("error occured")

# check if file exists
check = os.path.exists("./manage/files/n.txt")

# rm dir
if os.path.exists("./manage/files/newfolder"):
    os.rmdir("./manage/files/newfolder/")

# create folder
os.mkdir("./manage/files/newfolder")
