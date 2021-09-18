from sys import argv
amount, fraction = map(float, argv[1:])
tip = amount * fraction
print('tip = %s' % tip)
print('total = %s' % (amount + tip))
