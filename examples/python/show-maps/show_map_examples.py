import re
from invisibleroads_macros.disk import make_folder
from os.path import basename, join
from shutil import copy
from sys import argv


TARGET_FOLDER = make_folder(argv[1])
EXAMPLE_PATTERN = re.compile(r'_example.*')


def prepare_map(map_name, show_table=True):
    source_name = EXAMPLE_PATTERN.sub('', map_name)
    source_path = source_name + '.csv'
    target_path = join(TARGET_FOLDER, basename(source_path))
    copy(source_path, target_path)
    if show_table:
        print('%s_table_path = %s' % (map_name, target_path))
    print('%s_geotable_path = %s' % (map_name, target_path))


prepare_map('point_geometry_example')
prepare_map('point_geometry_example_dark', show_table=False)
prepare_map('point_geometry_example_streets_satellite', show_table=False)
prepare_map('wkt_geometry_example')

prepare_map('pixel_radius_example')
prepare_map('meter_radius_example')
prepare_map('range_radius_example')
prepare_map('mean_radius_example')
prepare_map('sum_radius_example')

prepare_map('the_specific_color_example')
prepare_map('mean_specific_color_example')
prepare_map('sum_specific_color_example')

prepare_map('red_scheme_color_example')
prepare_map('blue_scheme_color_example')
prepare_map('mean_blue_scheme_color_example')
prepare_map('sum_blue_scheme_color_example')
