
from __future__ import print_function

import sys
import os
import gzip

def zipupfolder(folder):
  with gzip.open( folder + '.gz', 'wb' ) as out:
    for fname in os.listdir(folder):
      with open( os.path.join(folder, fname) ) as f:
        for line in f:
          out.write(line)

def iter_dirs(meta_folder):
  for folder_name in os.listdir(meta_folder):
    folder = os.path.join(meta_folder, folder_name)
    print( 'Zipping up: {0}'.format(folder), file=sys.stderr )
    if folder.endswith('/'):
      folder = folder[:-1]
    print( 'Writing to: {0}'.format(folder + '.gz'), file=sys.stderr )
    zipupfolder(folder)

if __name__ == '__main__':
  if len(sys.argv) == 2:
    meta_folder = sys.argv[1]
    iterdirs(meta_folder)
