#!/usr/bin/env python3
# -*- coding: utf8 -*-

import os
import PyPDF2
from PIL import Image
from pathlib import Path
from filecmp import cmp


def find_size_zero_files(filepath):
    d = []
    for dirpath, dirnames, filenames in os.walk(filepath):
        for filename in filenames:
            if (os.stat(os.path.join(dirpath + "\\" + filename)).st_size == 0):
                if d == []:
                    print('\n\rSize-zero files:\n\r')
                d.append(os.path.join(dirpath + "\\" + filename))
                print(os.path.join(dirpath + "\\" + filename))



def find_corrupted_images(filepath):
    i = 0
    for dirpath, dirnames, filenames in os.walk(filepath):
        for filename in filenames:
            if filename.endswith('.jpg') or filename.endswith('.png') or (filename.endswith('.jpeg')):
                try:
                    img = Image.open(dirpath + '/' + filename)
                    img.verify()
                except (IOError, SyntaxError):
                    if i == 0:
                        i = 1
                        print('\n\rPotentially corrupted images:\n\r')
                    print(os.path.join(dirpath + "\\" + filename))



def find_corrupted_pdfs(filepath):
    i = 0
    for dirpath, dirnames, filenames in os.walk(filepath):
        for filename in filenames:
            if filename.endswith('.pdf'):
                try:
                    PyPDF2.PdfFileReader(dirpath + '\\' + filename, strict = False)
                except:  #(IOError, SyntaxError):
                    if i == 0:
                        i = 1
                        print('\n\rPotentially corrupted PDF files:\n\r')
                    print(os.path.join(dirpath + "\\" + filename))



def find_duplicated_files(filepath):
    # list of all documents
    DATA_DIR = Path(filepath)
    files = sorted(os.listdir(DATA_DIR))

    # List having the classes of documents
    # with the same content
    duplicateFiles = []

    # comparison of the documents
    for file_x in files:

        if_dupl = False

        for class_ in duplicateFiles:
            # Comparing files having same content using cmp()
            # class_[0] represents a class having same content
            if_dupl = cmp(
                DATA_DIR / file_x,
                DATA_DIR / class_[0],
                shallow=False
            )
            if if_dupl:
                class_.append(file_x)
                break

        if not if_dupl:
            duplicateFiles.append([file_x])

    print('\n\rPotentially duplicated files:\n\r')
    print(duplicateFiles)







if __name__ == '__main__':
    rootDir = input("Input top-level directory: ")
    if (rootDir[0] == "\"") or (rootDir[0] == "\'"):
        rootDir = rootDir.strip("\"")
        rootDir = rootDir.strip("\'")
    print("\n\rSearching in \"", rootDir, "\"...\n\r", sep = "")

    find_size_zero_files(rootDir)
    find_corrupted_images(rootDir)
    find_corrupted_pdfs(rootDir)
    find_duplicated_files(rootDir)





# webbrowser.open(dirpath + '/' + filename)
# pdfFileObj = os.startfile(dirpath + '/' + filename)

# # Check if the resource definition indicates this is a scanned PDF
# cmd = ['pdffonts', pdf_file]
# proc = subprocess.Popen(
#      cmd, stdout=subprocess.PIPE, bufsize=0, text=True, shell=False)
# out, err = proc.communicate()

# scanned = True

# for idx, line in enumerate(out.splitlines()):
#      if idx == 2:
#            scanned = False


          # # creating a pdf file object
          # pdfFileObj = open(dirpath + '/' + filename, 'rb')

          # # creating a pdf reader object
          # pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

          # # printing number of pages in pdf file
          # #print(pdfReader.numPages)

          # # creating a page object
          # #pageObj = pdfReader.getPage(0)

          # # extracting text from page
          # #print(pageObj.extractText())

          # # closing the pdf file object
          # pdfFileObj.close()


