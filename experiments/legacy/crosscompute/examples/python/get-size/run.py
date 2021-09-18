from os.path import getsize
from sys import argv

path = argv[1]
print('a_size = %s' % getsize(path))
