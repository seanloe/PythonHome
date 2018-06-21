#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, glob
from updver import search_file_for_string as ss

input_args = sys.argv

def main():
  #get current WORKSPACE directory
  if 'WORKSPACE' in os.environ:
      project_home = os.environ.get('WORKSPACE')
  else:
      print("WORKSPACE not set!")
      return
      
  #get project home directory
  #if 'PROJECT_PKG' in os.environ:
  #    project_package = os.environ.get('PROJECT_PKG')
  #else:
  #    print("PROJECT_PKG not set!")
  #    return
  if len(input_args) >2:
      search_file_ext = '**\\*.'+input_args[2]
  else:
      search_file_ext = '**\\*.c'
      
  search_key = input_args[1]

  
  final_path = project_home + '\\' + search_file_ext
  

  for filename in glob.iglob(final_path, recursive= True):
      ss(filename, search_key)
    
if __name__ == '__main__': main()