from sys import argv

x, y = argv[1:]
print('{} divided by {} is {}'.format(x, y, float(x) / float(y)))
