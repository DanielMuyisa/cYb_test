# fx lambda
# x = lambda a : a + 10
def x(a): return a+10


def x(a, b): return a * b

# anonmous fonction lambda


def anonymous_lambda(an):
    return lambda a: a * an


newfx = anonymous_lambda(5)
mlti = newfx(3)

print(mlti)
# lsx


def lambdas(n):
    return lambda a: a * n


callfx = lambdas(2)
print(callfx(4))
