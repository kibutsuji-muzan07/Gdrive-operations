import os
try:
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive
except ModuleNotFoundError:
    os.system('pip install PyDrive')
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive


def gauthentication(cred):
    gauth = GoogleAuth()
    if os.path.exists(cred):
        gauth.LoadCredentialsFile(cred)
    else:
        gauth.LocalWebserverAuth()
        gauth.SaveCredentialsFile(cred)

    drive = GoogleDrive(gauth)
    return drive


def create_folder(file_metadata, drive, folder_name):
    try:
        folderDetail = drive.ListFile({'q': "title = '"+folder_name+"' and trashed=false"}).GetList()[0]
        folder_id = folderDetail['id']
    except IndexError as IE:
        print(IE, " : No folder is there, creating one...")
        folder = drive.CreateFile(metadata=file_metadata)
        folder.Upload()
        folderDetail = drive.ListFile({'q': "title = '"+folder_name+"' and trashed=false"}).GetList()[0]
        folder_id = folderDetail['id']
    return folder_id


def upload_file(folder_id, drive, first_image, second_image, pdf, path):
    first_image_create = drive.CreateFile({'title': first_image, 'parents': [{'id': folder_id}]})
    first_image_create.SetContentFile(os.path.join(path, first_image))
    first_image_create.Upload()
    first_image_create = None

    second_image_create = drive.CreateFile({'title': second_image, 'parents': [{'id': folder_id}]})
    second_image_create.SetContentFile(os.path.join(path, second_image))
    second_image_create.Upload()
    second_image_create = None

    pdf_create = drive.CreateFile({'title': pdf, 'parents': [{'id': folder_id}]})
    pdf_create.SetContentFile(os.path.join(path, pdf))
    pdf_create.Upload()
    pdf_create = None


def search_file(folder_id, drive, first_image, second_image, pdf, path):
    try:
        first_image_link = drive.ListFile({'q': "title = '" + first_image + "' and trashed=false"}).GetList()[0]

        second_image_link = drive.ListFile({'q': "title = '" + second_image + "' and trashed=false"}).GetList()[0]

        pdf_link = drive.ListFile({'q': "title = '" + pdf + "' and trashed=false"}).GetList()[0]

    except:
        upload_file(folder_id, drive, first_image, second_image, pdf, path)

        first_image_link = drive.ListFile({'q': "title = '" + first_image + "' and trashed=false"}).GetList()[0]

        second_image_link = drive.ListFile({'q': "title = '" + second_image + "' and trashed=false"}).GetList()[0]

        pdf_link = drive.ListFile({'q': "title = '" + pdf + "' and trashed=false"}).GetList()[0]

    return first_image_link, second_image_link, pdf_link


def get_link(folder_id, drive, first_image, second_image, pdf, path):
    first_image_link, second_image_link, pdf_link = search_file(folder_id, drive, first_image, second_image, pdf, path)
    first_image_link = first_image_link['alternateLink']
    second_image_link = second_image_link['alternateLink']
    pdf_link = pdf_link['alternateLink']

    return str(first_image_link), str(second_image_link),  str(pdf_link)
