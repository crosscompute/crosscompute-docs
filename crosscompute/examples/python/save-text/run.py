from os.path import join
from sys import argv

target_file = open(join(argv[1], 'xyz.txt'), 'w')
target_file.write('Repeatedly try to start productive tasks')
