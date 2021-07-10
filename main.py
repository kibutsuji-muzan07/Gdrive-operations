from driveauth import *
from write_to_csv import writer
import sys
import yaml


def main(first_image, second_image, pdf, path, csv_file, folder_name, cred):
    file_metadata = {
        'title': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    drive = gauthentication(cred)
    folder_id = create_folder(file_metadata, drive, folder_name)
    first_image_link, second_image_link, pdf_link = get_link(folder_id, drive, first_image, second_image, pdf, path)
    url_list = [first_image_link, second_image_link, pdf_link]
    writer(url_list, csv_file)


if __name__ == '__main__':
    first_image = str(sys.argv[1])
    second_image = str(sys.argv[2])
    pdf = str(sys.argv[3])
    path = str(sys.argv[4])
    config = open("config.yml")
    parsed_config = yaml.load(config, Loader=yaml.FullLoader)
    csv_file = parsed_config['csv_file']
    folder_name = parsed_config['folder_name']
    cred = parsed_config['configured_cred']
    main(first_image, second_image, pdf, path, csv_file, folder_name, cred)
