#### read_header

import numpy as np
import os, glob, sys
import struct

class BinaryReader():
    # Map well-known type names into struct format characters.
    name='Carlton'
    typeNames = {
        'int8'   :'b',
        'uint8'  :'B',
        'int16'  :'h',
        'uint16' :'H',
        'int32'  :'i',
        'uint32' :'I',
        'int64'  :'q',
        'uint64' :'Q',
        'float'  :'f',
        'double' :'d',
        'char'   :'s'}

class header():
    """This header is equivalent to struct"""
    pass

def read_header(file,path,nest):
    """" The function reads the flexpart output header file +  grid_files which are also haéader files
    Options ::
    file = filename
    path = path to add to to the header
    nest = value for nested(1) or non nested data(0)"""

    print('This is the file we read'+file)

    header.path=path

    #### checks if files are nested or not.Opens the files. CHecks files
    if nest==0:
        print('No nested files')
        try:
            fd=open(file,'rb').read()
            print('File opened')
            frd = 1 ## file read constant
        except IOError:
            print('No file. ERROR!!!!! FIND THE FILES')
            sys.exit(1)
    else:
      print('Nested file')

    header.decayconstant=0

    if frd==1:
        print('BLAHBLAH')

    return;
