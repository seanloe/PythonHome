#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import glob
from time import sleep

def replace_string(filename, keystring, value):
    print('Replacing version string...')
    f = open(filename, 'r+', encoding = 'shift-jis')
    line = f.readline()
    while line != '':
        if keystring in line:
            stringlist = line.split(' ')
            spacecount = stringlist.count('')
            for i in range(spacecount):
                stringlist.remove('')
            tokenindex = stringlist.index(keystring)+2
            offset = line.find(stringlist[tokenindex])
            f.seek((f.tell()-len(line))+line.find(keystring)-1+offset)
            f.write(value)
            f.tell() # strnage. without this line. string will be append to the end of file
        line = f.readline()
    f.close()
    
def search_file_for_string(filename,keystring):
    try:
        with open(filename, 'r', encoding = 'shift-jis') as f:
            filebuff = f.read()
    except UnicodeDecodeError:
        try:
            with open(filename, 'r', encoding = 'utf-8') as f:
                filebuff = f.read()
        except UnicodeDecodeError:
            print("+======================+")
            print("Unknown char encoding!!")
            print("skip "+filename)
            print("+======================+")
            
    try:        
        if keystring in filebuff:
            print("Found \'%s\' in " %keystring + filename )
            for num, line in enumerate(filebuff.splitlines(1),1):
                if keystring in line:
                    if(line.find(keystring) < line.find('=')):
                        #print(num, line)
                        return True
            print("Not a set value phrase!")
            return False
        else:
            return False
    except:
        pass

        
def main():
  #get current WORKSPACE directory
  if 'WORKSPACE' in os.environ:
      project_home = os.environ.get('WORKSPACE')
  else:
      print("WORKSPACE not set!")
      return
      
  #get project home directory
  if 'PROJECT_PKG' in os.environ:
      project_package = os.environ.get('PROJECT_PKG')
  else:
      print("PROJECT_PKG not set!")
      return
      
  search_file_ext = '**\\*.env'
  final_path = project_home + '\\' +project_package + '\\' + search_file_ext
  (majorver, minorver) = sys.argv[1].split('.')

  for filename in glob.iglob(final_path, recursive= True):
      if search_file_for_string(filename, 'FJ_BIOS_MAJOR_VERSION'):
          replace_string(filename, 'FJ_BIOS_MAJOR_VERSION', majorver)
          replace_string(filename, 'FJ_BIOS_MINOR_VERSION', minorver)
    
if __name__ == '__main__': main()