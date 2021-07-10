import csv


def writer(links, csv_file):
    with open(csv_file, mode='w') as link:
        links_writer = csv.writer(link, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        links_writer.writerow(links)
