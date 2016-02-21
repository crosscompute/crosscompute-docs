from csv import DictReader
from sys import argv

x, text_path, table_path = argv[1:]
print('x = %s' % x)
print('text = %s' % open(text_path).read().strip())
print('table.columns = %s' % DictReader(open(table_path)).fieldnames)
