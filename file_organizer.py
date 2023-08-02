# python file_organizer.py

import os
import shutil

EX_DICT = {
    'pdf': 'OneDrive/Dokumente',
    'doc': 'OneDrive/Dokumente',
    'docx': 'OneDrive/Dokumente',
    'txt': 'OneDrive/Dokumente',
    'html': 'OneDrive/Dokumente',
    'htm': 'OneDrive/Dokumente',
    'xls': 'OneDrive/Dokumente',
    'xlsx': 'OneDrive/Dokumente',
    'ppt': 'OneDrive/Dokumente',
    'pptx': 'OneDrive/Dokumente',
    'odp': 'OneDrive/Dokumente',
    'key': 'OneDrive/Dokumente',
    'jpg': 'OneDrive/Bilder',
    'jpeg': 'OneDrive/Bilder',
    'png': 'OneDrive/Bilder',
    'gif': 'OneDrive/Bilder',
    'webp': 'OneDrive/Bilder',
    'tif': 'OneDrive/Bilder',
    'tiff': 'OneDrive/Bilder',
    'mp4': 'Videos',
    'avi': 'Videos',
    'flv': 'Videos',
    'wmv': 'Videos',
    'mov': 'Videos',
    'avchd': 'Videos',
    'm4a': 'Musik',
    'm4b': 'Musik',
    'mp3': 'Musik',
    'wav': 'Musik',
}

file_path, extension, target_folder = '', '', ''
base_dir = 'C:/Users/esdea/'
od_dir = 'C:/Users/esdea/OneDrive/'
dl_dir = 'C:/Users/esdea/Downloads/'
none_dir = 'C:/Users/esdea/OneDrive/Undefined/'

'''
OneDrive
'''
for filename in os.listdir(od_dir):
    f = os.path.join(od_dir, filename)

    if os.path.isfile(f):
        file_path = od_dir + filename
        extension = filename.split(".")[-1]

        if extension in EX_DICT:
            target_folder = base_dir + EX_DICT.get(extension)
            shutil.move(file_path, target_folder)

'''
Downloads
'''
for filename in os.listdir(dl_dir):
    f = os.path.join(dl_dir, filename)

    if os.path.isfile(f):
        file_path = dl_dir + filename
        extension = filename.split(".")[-1]

        if extension in EX_DICT:
            target_folder = base_dir + EX_DICT.get(extension)
            shutil.move(file_path, target_folder)