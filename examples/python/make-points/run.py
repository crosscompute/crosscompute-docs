import csv
from argparse import ArgumentParser
from invisibleroads_macros.disk import make_enumerated_folder_for, make_folder
from invisibleroads_macros.log import format_summary
from os.path import join
from random import randint


def run(target_folder, point_count, x_min, x_max, y_min, y_max):
    target_path = join(target_folder, 'points.csv')
    csv_writer = csv.writer(open(target_path, 'w'))
    csv_writer.writerow(['x', 'y'])
    for index in range(point_count):
        x = randint(x_min, x_max)
        y = randint(y_min, y_max)
        csv_writer.writerow([x, y])
    return [
        ('point_table_path', target_path),
    ]


if __name__ == '__main__':
    argument_parser = ArgumentParser()
    argument_parser.add_argument(
        '--target_folder',
        metavar='FOLDER', type=make_folder)

    argument_parser.add_argument(
        '--point_count',
        metavar='COUNT', type=int, required=True)
    argument_parser.add_argument(
        '--x_min',
        metavar='FOLDER', type=int, required=True)
    argument_parser.add_argument(
        '--x_max',
        metavar='FOLDER', type=int, required=True)
    argument_parser.add_argument(
        '--y_min',
        metavar='FOLDER', type=int, required=True)
    argument_parser.add_argument(
        '--y_max',
        metavar='FOLDER', type=int, required=True)

    args = argument_parser.parse_args()
    d = run(
        args.target_folder or make_enumerated_folder_for(__file__),
        args.point_count,
        args.x_min,
        args.x_max,
        args.y_min,
        args.y_max)
    print(format_summary(d))
