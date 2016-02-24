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


prepare_map('geometry_point_example')
prepare_map('geometry_point_example_dark', show_table=False)
prepare_map('geometry_point_example_streets_satellite', show_table=False)
prepare_map('geometry_wkt_example')

prepare_map('radius_meter_example')
prepare_map('radius_pixel_example')
prepare_map('radius_pixel_range_example')
prepare_map('radius_pixel_mean_example')
prepare_map('radius_pixel_sum_example')

prepare_map('specific_color_example')
prepare_map('specific_color_mean_example')
prepare_map('specific_color_sum_example')

prepare_map('color_scheme_red_example')
prepare_map('color_scheme_blue_example')
prepare_map('color_scheme_blue_mean_example')
prepare_map('color_scheme_blue_sum_example')
