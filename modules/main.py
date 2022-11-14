# import only on element in a module
from buildin_modules import sys as s
import custom_modules as md

md.sayHello()
print('Current sys : ' + s)
