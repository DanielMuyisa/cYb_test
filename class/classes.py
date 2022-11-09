class Network:
    z = 'zone'
    r = 'router'
    s = ' switch'
    f = 'fil'

    # construct
    def __init__(self, z, r, s, f):
        self.z = z
        self.r = r
        self.s = s
        self.f = f


# fake way
tool = Network('zone', 'router', 'switch', 'fills')
print(tool.f)

# always executed when the class is being initiated.
