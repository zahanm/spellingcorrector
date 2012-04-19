
from __future__ import print_function

import sys
import os
import gzip
import itertools

from random import random

def assemble_query_data(clean_fname, misspelled_fname, google_fname):
  """
  want to build up queries = [ .. , (misspelled, clean, google), .. ]
  usage: corrupt, clean, google = datagen.assemble_query_data('data/strings_clean.txt', 'data/strings_corrupted.txt', 'data/strings_googlespell.txt')
  """
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
  google = [ None ] * len(clean)
  with open(google_fname) as google_f:
    for line in google_f:
      corrupt, attempt = line.rstrip().split(':')
      # will throw an error if it doesn't exist
      attempt = attempt.lstrip()
      i = misspelled.index(corrupt)
      try:
        if misspelled[i+1:].index(corrupt):
          import pdb; pdb.set_trace()
      except ValueError:
        pass
      google[i] = attempt
  # with open('./data/queries.txt', 'w') as queries:
  #   with open('./data/gold.txt', 'w') as gold:
  #     with open('./data/test.txt', 'w') as test:
  #       for i in xrange(len(clean)):
  #         if random() < 0.5:
  #           # dev set
  #           queries.write( misspelled[i] + '\n' )
  #           gold.write( "{0}\t{1}\n".format( clean[i], google[i]) )
  #         else:
  #           # test set
  #           test.write( "{0}\t{1}\t{2}\n".format( misspelled[i], clean[i], google[i]) )
  with open('./data/strings_googlereorder.txt', 'w') as goog:
    for i, l in enumerate(google):
      if l == None:
        import pdb; pdb.set_trace()
      goog.write( l + '\n' )
  return (misspelled, clean, google)

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
  if len(sys.argv) == 4:
    assemble_query_data(sys.argv[1], sys.argv[2], sys.argv[3])
