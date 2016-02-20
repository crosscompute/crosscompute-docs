from csv import DictReader
from sys import argv

x, y, z, text_path, table_path = argv[1:]
print('x = %s' % x)
print('y = %s' % y)
print('z = %s' % z)
print('text = %s' % open(text_path).read().strip())
print('table.columns = %s' % DictReader(open(table_path)).fieldnames)
