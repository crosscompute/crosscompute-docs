import sys
from os.path import getsize
path = sys.argv[1]
print('a_size = %s' % getsize(path))
