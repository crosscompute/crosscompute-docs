from argparse import ArgumentParser
from crosscompute_table import TableType
from invisibleroads_macros.disk import make_enumerated_folder_for, make_folder
from invisibleroads_macros.log import format_summary
from os.path import join


def run(target_folder, map_table_name, map_table):
    target_path = join(target_folder, 'map.csv')
    map_table.to_csv(target_path, index=False)
    return [(map_table_name + '_path', target_path)]


if __name__ == '__main__':
    argument_parser = ArgumentParser()
    argument_parser.add_argument(
        '--target_folder',
        metavar='FOLDER', type=make_folder)

    argument_parser.add_argument(
        '--map_table_name',
        metavar='NAME', required=True)
    argument_parser.add_argument(
        '--map_table_path',
        metavar='PATH')

    args = argument_parser.parse_args()
    d = run(
        args.target_folder or make_enumerated_folder_for(__file__),
        args.map_table_name,
        TableType.load(args.map_table_path))
    print(format_summary(d))
