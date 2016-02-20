import csv
import sys
from collections import Counter
from invisibleroads_macros.disk import make_folder
from invisibleroads_macros.text import compact_whitespace
from os.path import join


target_folder, text_path = sys.argv[1:]
character_counter = Counter(compact_whitespace(open(text_path).read()))
del character_counter[' ']
target_path = join(make_folder(target_folder), 'character_count.csv')
csv_writer = csv.writer(open(target_path, 'w'))
csv_writer.writerows(character_counter.most_common())
print('character_count_table_path = ' + target_path)
