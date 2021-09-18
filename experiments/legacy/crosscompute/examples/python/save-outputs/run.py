import matplotlib
matplotlib.use('Agg')  # Prevent no $DISPLAY environment variable warning

from invisibleroads_macros.disk import make_folder
from matplotlib import pyplot as plt
from os.path import join
from sys import argv

target_folder = make_folder(argv[1])
# Render integer
print('an_integer = 100')
# Render table
target_path = join(target_folder, 'a.csv')
open(target_path, 'w').write("""\
a,b,c
1,2,3
4,5,6
7,8,9""")
print('a_table_path = ' + target_path)
# Render image
target_path = join(target_folder, 'a.png')
figure = plt.figure()
plt.plot([1, 2, 3], [1, 2, 2])
figure.savefig(target_path)
print('an_image_path = ' + target_path)
# Render geotable (map)
target_path = join(target_folder, 'b.csv')
open(target_path, 'w').write("""\
Latitude,Longitude,Description
27.3364347,-82.5306527,A
27.3364347,-82.5306527,B
25.7616798,-80.1917902,C
25.7616798,-80.1917902,D
""")
print('a_geotable_path = ' + target_path)
