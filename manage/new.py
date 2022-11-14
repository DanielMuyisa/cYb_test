path = "./manage/files/new_file_test.txt"
try:
    n = open(path, 'a')
    n.write("All people seens to need data processing")
    n.close()
    print(n)
except NameError:
    print("path not found")
