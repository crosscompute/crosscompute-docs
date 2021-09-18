import csv
from geopy import GoogleV3
from invisibleroads_macros.disk import make_folder
from os.path import join
from sys import argv

target_folder, address_text_path = argv[1:]
geocode = GoogleV3().geocode
location_table_path = join(make_folder(target_folder), 'locations.csv')
csv_writer = csv.writer(open(location_table_path, 'w'))
csv_writer.writerow(['Address', 'Latitude', 'Longitude'])
for address in open(address_text_path):
    location = geocode(address)
    csv_writer.writerow([
        address.strip(), location.latitude, location.longitude])
print('location_table_path = ' + location_table_path)
