from invisibleroads_macros.disk import make_folder
from os.path import basename, join
from shutil import copy
from sys import argv

target_folder = make_folder(argv[1])
# Point
source_path = 'point_geometry.csv'
target_path = join(target_folder, basename(source_path))
copy(source_path, target_folder)
print('point_geometry_example_table_path = ' + target_path)
print('point_geometry_example_geotable_path = ' + target_path)
# Geometry
# print('wkt_geometry_example_geotable_path = ')

# Base
# print('tile_example_dark_geotable_path')
# print('tile_example_streets_satellite_geotable_path')

# Radius in pixels
# print('pixel_radius_example_geotable_path')
# Radius in meters
# print('meter_radius_example_geotable_path')
# Radius range
# print('range_radius_example_geotable_path')
# Radius from mean
# print('mean_radius_example_geotable_path')
# Radius from sum
# print('sum_radius_example_geotable_path')

# Fill color
# !! all variations
# single letter
# 0-1 grey shades
# hex string
# rgb tuple
# html names
# print('specific_color_example_geotable_path')
# print('mean_specific_color_example_geotable_path')
# print('sum_specific_color_example_geotable_path')
# from mean sum

# Fill color scheme
# from mean sum
# print('scheme_color_example_geotable_path')
# print('mean_scheme_color_example_geotable_path')
# print('sum_scheme_color_example_geotable_path')
