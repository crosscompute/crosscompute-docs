import sys
from os.path import join
target_file = open(join(sys.argv[1], 'xyz.txt'), 'w')
target_file.write('Repeatedly try to start productive tasks')
