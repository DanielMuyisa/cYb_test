try:
    print(x)
except NameError:
    print("Var x doesn't exists")
except:
    print("An other error occurred")
finally:
    print("end")


# raise exeption where condition faild
x = 2
answers = (0, 3, 2, 4, 5, 7, 5, 1, 9, 6)
if x in answers:
    raise Exception("unsupported")


if type(x) is int:
    raise TypeError("Only integers are allowed")
