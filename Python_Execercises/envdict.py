#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import glob
import pickle



def getenv():
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
    final_search_path = project_home + '\\' +project_package + '\\' + search_file_ext
    #create environment variable dict struture
    env_dic = {}
    
    for filename in glob.iglob(final_search_path, recursive= True):
        #
        #print('Processing %s...'% filename)
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
            for lines in filebuff.splitlines(1):
                if '=' in lines:
                    #print(lines)
                    stringlist = lines.split(' ')
                    spacecount = stringlist.count('')
                    for _ in range(spacecount):
                        stringlist.remove('')
                    key = stringlist[stringlist.index('=')-1]
                    value = stringlist[stringlist.index('=')+1]
                    value = value.replace('\n','')
                    env_dic[key] = value
                    #print('key=',key,end='')
                    #print(' value=',value)
                else:
                    pass
                    #print('Can not find a "="')
            #print(env_dic)
        except:
            pass
    #print('Major version =',env_dic['FJ_BIOS_MAJOR_VERSION'])
    #print('Mainor version =',env_dic['FJ_BIOS_MINOR_VERSION'])
    pk_file = project_package+'.pickle'
    if os.path.exists(pk_file):
        #remove old record
        os.remove(pk_file)
    with open(pk_file,'wb') as f:
        pickle.dump(env_dic,f)

def main():
    getenv()
    
if __name__ == '__main__': main()