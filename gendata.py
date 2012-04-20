
from __future__ import print_function

import sys
import os
import gzip
import itertools

from random import random

def pick_unmodified(clean, misspelled, google):
  with open('data/queries/clean.txt', 'w') as clean_f:
    with open('data/queries/misspelled.txt', 'w') as misspelled_f:
      with open('data/queries/google.txt', 'w') as google_f:
        for i in xrange(len(clean)):
          if random() < 0.5:
            # use corrupted query
            clean_f.write( clean[i] + '\n' )
            misspelled_f.write( misspelled[i] + '\n' )
            google_f.write( google[i] + '\n' )
          else:
            # use clean query
            clean_f.write( clean[i] + '\n' )
            misspelled_f.write( clean[i] + '\n' )
            google_f.write( clean[i] + '\n' )

def split_train_test(clean, misspelled, google):
  with open('data/final/queries.txt', 'w') as queries:
    with open('data/final/gold.txt', 'w') as gold:
      with open('data/final/test.txt', 'w') as test:
        for i in xrange(len(clean)):
          if random() < 0.5:
            # dev set
            queries.write( misspelled[i] + '\n' )
            gold.write( "{0}\t{1}\n".format( clean[i], google[i]) )
          else:
            # test set
            test.write( "{0}\t{1}\t{2}\n".format( misspelled[i], clean[i], google[i]) )

def reorder_clean_google(clean, misspelled, bad_google):
  google = [ None ] * len(misspelled)
  for g in bad_google:
    try:
      q, attempt = g.split(':')
    except ValueError:
      import pdb; pdb.set_trace()
    i = misspelled.index(q)
    if not attempt:
      google[i] = misspelled[i]
    else:
      google[i] = attempt.lstrip()
    if not google[i].strip():
      import pdb; pdb.set_trace()
  with open('data/queries/newgoogle.txt', 'w') as out:
    for attempt in google:
      out.write( attempt + '\n' )

def read_query_data(clean_fname, misspelled_fname, google_fname):
  """
  want to build up queries = [ .. , (clean, misspelled, google), .. ]
  usage: clean, misspelled, google = gendata.assemble_query_data('data/strings_clean.txt', 'data/strings_corrupted.txt', 'data/strings_googlespell.txt')
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
  with open(google_fname) as google_f:
    for line in google_f:
      google.append( line.rstrip() )
  assert( len(google) == len(clean) )
  return (clean, misspelled, google)

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

def num_lines(fname):
  count = 0
  with gzip.open(fname) as f:
    for line in f:
      if line.strip():
        count += 1
  print( 'num lines: ' + str(count) )
  return count

if __name__ == '__main__':
  if len(sys.argv) == 4:
    clean, misspelled, google = read_query_data(sys.argv[1], sys.argv[2], sys.argv[3])
    # import pdb; pdb.set_trace()
    # pick_unmodified( clean, misspelled, google )
    reorder_clean_google(clean, misspelled, google)
  elif len(sys.argv) == 2:
    num_lines(sys.argv[1])
