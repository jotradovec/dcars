import os
from zipfile import ZipFile


def zip_directories(files_and_dirs, output_filename):
    with ZipFile(output_filename, 'w') as zipf:
        for item in files_and_dirs:
            if os.path.isdir(item):
                for root, _, files in os.walk(item):
                    for file in files:
                        file_path = str(os.path.join(root, file))
                        arcname = os.path.relpath(file_path, os.path.join(item, '..'))
                        zipf.write(filename=file_path, arcname=arcname)
            else:
                zipf.write(filename=item, arcname=os.path.basename(item))


if __name__ == '__main__':
    # Specify directories and files to include in the archive
    files_and_dirs = ['cars', 'dcars', '.ebextensions', 'manage.py', 'requirements.txt', '.env']
    output_file = 'to_deploy.zip'

    # Create zip archive
    zip_directories(files_and_dirs, output_file)
    print('Done')
