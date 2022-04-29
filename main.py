#!/usr/bin/env python3
# -*- coding: utf8 -*-

import os
# import pikepdf
import PyPDF2
from PIL import Image



def find_size_zero_files(filepath):
    ##  Find empty files
    d = []
    for dirpath, dirnames, filenames in os.walk(filepath):
        for filename in filenames:
            #print(filename)
            if (os.stat(os.path.join(dirpath + "\\" + filename)).st_size == 0) and d == []:
                ## Print the names of potentially corrupted files
                print('\n\rSize-zero files:\n\r')
                d.append(os.path.join(dirpath + "\\" + filename))
                print(os.path.join(dirpath + "\\" + filename))
            elif os.stat(os.path.join(dirpath + "\\" + filename)).st_size == 0:
                d.append(os.path.join(dirpath + "\\" + filename))
                print(os.path.join(dirpath + "\\" + filename))
    return


## PDFs
def find_corrupted_pdfs(filepath):
    ##  Find corrupt pdfs
    potentially_corrupted_files = []
    pdfCount = 0
    badFileCount = 0
    for dirpath, dirnames, filenames in os.walk(filepath):
        for filename in filenames:
            if os.stat(os.path.join(dirpath + "\\" + filename).endswith('.pdf')):
                 potentially_corrupted_files.append(os.path.join(dirpath + "\\" + filename))
                 # print(os.path.join(dirpath + "\\" + filename + "\n"))
            # if filename.endswith('.pdf'):
                 pdfCount = pdfCount + 1
                 try:
                    PyPDF2.PdfFileReader(dirpath + '\\' + filename)
                 except:
                    if(badFileCount == 0):
                        # print('Potentially corrupted files: ')
                        potentially_corrupted_files = potentially_corrupted_files.append(os.path.join(dirpath + "\\" + filename + "\n"))
                    badFileCount = badFileCount + 1
                    print(str(badFileCount) + ')  ' + dirpath + '\\' + filename)
    print('Total Number of PDF files found:  ' + str(pdfCount))
    print('Number of potentially corrupted PDF files found:  ' + str(badFileCount) + '\n')
    print('Potentially corrupted files: ')
    # print(potentially_corrupted_files)
    return potentially_corrupted_files



def find_corrupted_images(dirpath):
     for filename in os.listdir(dirpath):
          if filename.endswith('.jpg') or filename.endswith('.png'):
                try:
                    img = Image.open(dirpath + '/' + filename)
                    img.verify()
                except (IOError, SyntaxError):
                    ## Print the names of potentially corrupted files
                    print('\n\rPotentially corrupted files:\n\r')
                    print(os.path.join(dirpath + "\\" + filename))


## Find corrupted image files
def get_corrupted_images(filepath):
    d = []
    for dirpath, dirnames, filenames in os.walk(filepath):
        for filename in filenames:
            filename = str.lower(filename)
            if (filename.endswith('.png')) or (filename.endswith('.jpg')) or (filename.endswith('.jpeg')):
                try:
                  img = Image.open(os.path.join(dirpath, filename))  # open the image file
                  img.verify() # verify that it is, in fact, an image
                  img.close()
                except (IOError, SyntaxError):
                  d.append(os.path.join(dirpath + "\\" + filename))
                  #print('Bad file:', os.path.join(dirpath + "\\" + filename)) # print out the names of corrupt files
    return d


def find_duplicate_files(filepath):
    pass


if __name__ == '__main__':
    rootDir = input("Input top-level directory: ")
    if (rootDir[0] == "\"") or (rootDir[0] == "\'"):
        rootDir = rootDir.strip("\"")
        rootDir = rootDir.strip("\'")
    print("\n\rSearching in \"", rootDir, "\"...\n\r", sep = "")

    find_size_zero_files(rootDir)
    find_corrupted_images(rootDir)
    #find_corrupt_pdfs(r"C:\Users\Jay\Desktop\Drive_Management\FileMetaDataManager\ExampleDirectory")
    #checkPDFs(dirpath = "D:/Drive_Three/Library/Admin Programs")

     # print("""\
     # Usage: thingy [OPTIONS]
     #      -h                        Display this usage message
     #      -H hostname               Hostname to connect to
     # """)





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



##  Basic directory traversal
##  Import the os module, for the os.walk function
#import os

# '''
# import os, sys
# os.chdir("C:\\Users\\jborthen\\Desktop\\FileMetaDataManager")
# execfile("BasicDirectoryTraversal.py")
# '''

# rootDir = input("Input top-level directory: ")
# print('\r\n')
# for fullPath, subdirList, fileList in os.walk(rootDir):
# 	folderName=str(fullPath).split(rootDir)
# 	print(('\t'*str(folderName[1]).count('\\'))+ '+ Found directory: "...%s"\r\n' % folderName[1])
# 	for i, fname in enumerate(fileList, start=1):
# 		print('{:<45}'.format(('\t'*(1+str(folderName[1]).count('\\')))+str(i)+")  "+fname)+'{:<5}'.format("Size: ") + '{:>12}'.format(str(round(((os.stat(fullPath+"\\"+fname)[6])/1000.0),1))+" KB"))
# 	print('\r\n')

