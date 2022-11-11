# download packages with pip
import camelcase
cml = camelcase.CamelCase()

st = 'Partout le roi trouve son siege assit'

rs = cml.hump(st)

print(rs)
