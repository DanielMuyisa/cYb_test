import datetime
import platform

# sys
sys = platform.system()
print(sys)

s = platform.architecture()
s = platform.machine()
s = platform.uname()
# print(s)

# lisr all the function names of a module
# lst = dir(platform)
# print(lst)


# DATE
date = datetime.datetime.now()
# print(date.strftime("%A"))
# -- date obj
print(datetime.datetime(2022, 10, 10))
