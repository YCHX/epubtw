from simpleEpub import epub
from opencc import OpenCC
from bs4 import BeautifulSoup
import os
import shutil
from multiprocessing import Pool

def convert_text(input_text):
    cc = OpenCC('s2tw')  # Create a converter from Simplified to Traditional Chinese (Taiwan)
    return cc.convert(input_text)

def process_xhtml(xhtml):
    with open(xhtml, 'r') as f:
        content = f.read()
    soup = BeautifulSoup(content, 'html.parser')
    body = soup.find('body')
    if body:
        text_nodes = body.find_all(string=True)
        for node in text_nodes:
            node.replace_with(convert_text(node))
        with open(xhtml, 'w') as f:
            f.write(str(soup))

# def process(input_path, output_name):
#     folder = epub.extract_epub(input_path, os.path.join(os.path.dirname(input_path), os.path.splitext(output_name)[0]))
#     xhtmls = epub.find_xhtml_files(folder)
#     for xhtml in xhtmls:
#         with open(xhtml, 'r') as f:
#             content = f.read()
#         soup = BeautifulSoup(content, 'html.parser')
#         body = soup.find('body')
#         if body:
#             text_nodes = body.find_all(string=True)
#             for node in text_nodes:
#                 node.replace_with(convert_text(node))
#             with open(xhtml, 'w') as f:
#                 f.write(str(soup))
        
#     epub.pack_epub(folder, output_name)
#     shutil.rmtree(folder)

def process_xml(filename):
    with open(filename, 'r') as f:
        content = f.read()
    soup = BeautifulSoup(content, 'xml')
    text_nodes = soup.find_all(['text'])
    if soup.find('metadata'):
        metadata = soup.select_one('metadata')
        text_nodes.extend(metadata.find_all(True))
    for node in text_nodes:
        if node.string:
            node.string.replace_with(convert_text(node.string))
    with open(filename, 'w') as f:
        f.write(str(soup))

def process(input_path, output_name):
    output_folder = os.path.join(os.path.dirname(input_path), os.path.splitext(output_name)[0])
    folder = epub.extract_epub(input_path, output_folder)
    xhtmls = epub.find_xhtml_files(folder)
    xmls = epub.find_xml_files(folder)
    
    with Pool() as pool:
        pool.map(process_xhtml, xhtmls)
        pool.map(process_xml, xmls)

    epub.pack_epub(folder, output_name)
    shutil.rmtree(folder)

# For testing
if __name__ == '__main__':
    input_path = '由最凶恶魔王所锻炼的勇者，在异世界回归者们的学园里所向披靡 02.epub'
    output_name = convert_text(f'[Converted]{os.path.basename(input_path)}')
    process(input_path, output_name)