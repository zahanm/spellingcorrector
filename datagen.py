
from __future__ import print_function

import sys
import os
import gzip
import itertools

def assemble_query_data(clean_fname, misspelled_fname, google_fname):
  # want to build up queries = [ .. , (misspelled, clean, google), .. ]
  queries = []
  clean = []
  misspelled = []
  google = []
  with open(clean_fname) as clean_f:
    for line in clean_f:
      clean.append( line.rstrip() )
  with open(misspelled_fname) as misspelled_f:
    for line in misspelled_f:
      misspelled.append( line.rstrip() )
  assert( len(clean) == len(misspelled) )
  with open(google_fname) as google_f:
    for line in google_f:
      a, b = line.rstrip().split(':')
        query_results.append( (clean.rstrip(), misspelled.rstrip()) )

def assemble_edit1s(clean_fname, misspelled_fname):
  edit1s = []
  # [ .. , ( misspelled, clean ), .. ]
  with open(clean_fname) as clean:
    with open(misspelled_fname) as misspelled:
      for line_clean, line_misspelled in itertools.izip(clean, misspelled):
        edit1s.append( (line_misspelled.rstrip(), line_clean.rstrip()) )
  with gzip.open('data/edit1s.txt.gz', 'wb') as out:
    for tup in edit1s:
      out.write( "{0}\t{1}\n".format(tup[0], tup[1]) )

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
  if len(sys.argv) == 3:
    clean_edit1s = sys.argv[1]
    misspelled_edit1s = sys.argv[2]
    assemble_edit1s(clean_edit1s, misspelled_edit1s)
