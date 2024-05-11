from zipfile import ZipFile
import os

def extract_epub(path, dst):
    with ZipFile(path, 'r') as zip_ref:
        zip_ref.extractall(dst)
    return dst

# def pack_epub(src, dst, name):
#     path = os.path.join(dst, name)
#     os.chdir(src)
#     with ZipFile(path, 'w', 0) as zip_ref:
#         for root, dirs, files in os.walk('.'):
#             for file in files:
#                 if file != '.DS_Store' and not root.startswith('__MACOSX'):
#                     zip_ref.write(os.path.join(root,file))

def pack_epub(folder, name):
    path = os.path.join(os.path.dirname(folder), name)

    with ZipFile(path, 'w', 0) as zip_ref:
        for root, dirs, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, folder)
                if file != '.DS_Store' and not root.startswith('__MACOSX'):
                    zip_ref.write(file_path, rel_path)

def find_xhtml_files(src):
    text_files = []
    for root, dirs, files in os.walk(src):
        for file in files:
            if file.endswith('.xhtml'):
                text_files.append(os.path.join(root, file))
    return text_files

def find_xml_files(src):
    text_files = []
    for root, dirs, files in os.walk(src):
        for file in files:
            if file.endswith('.ncx') or file.endswith('.opf'):
                text_files.append(os.path.join(root, file))
    return text_files


