#!/usr/bin/env python
# Akshay Singh
# Decrypt encrypted zip files using bruteforce

import zipfile
import sys
from threading import Thread

def checkZip(zipName): #checking if zip file is in the directory
    try:
        zipFile = zipfile.ZipFile(zipName)
        return True
    except:
        print("Error "+zipName+" is not in the directory")
        return False

def decryptZip(zipName,dictWord): #decrypt encrypted zip file
    try:
        zipFile = zipfile.ZipFile(zipName)
        zipFile.extractall(pwd=dictWord)
        print("[-] "+"Password Found: "+dictWord)
        return 
    except:
        return

def main():
    zipName = str(raw_input("Enter the name of the encrypted zip file(add .zip): "))
    dictName = str(raw_input("Enter the name of the dictionary file(add .txt): "))

    if(checkZip(zipName) == False): #closing the program if the zip is not found
        sys.exit()
    else:
        try:
            dictFile = open(dictName, "r")
            for words in dictFile.readlines():
                words = words.strip('\n')
                print("[+] "+"Trying word: "+words)
                t = Thread(target=decryptZip, args=(zipName,words))
                t.start()
        except:
            print("Error cannot find the dictionary "+dictName)

if __name__ == "__main__":
    main()
