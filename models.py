
import sys
import random
import itertools
import cPickle as pickle

from collections import Counter

training_corpus_loc = './data/corpus/'
edit1s_loc = './data/edit1s.txt'

def walk_pairs():
  """
  `itertools` is a module with useful iteration functions like izip( .. )
  The `numbers[1:]` is an example of list slices
  """
  numbers = range(10)
  for tup in itertools.izip( numbers[:-1], numbers[1:] ):
    print(tup)

def count_ints():
  """
  Counter is a specialized dictionary optimized for keeping counts
  A notable difference is that the count for a missing item is zero (rather than raise a KeyError)
  Read up on it here: http://docs.python.org/library/collections.html#counter-objects
  """
  counts = Counter()
  for i in xrange(100000):
    num = random.randint(10)
    counts[ num ] += 1
  assert( sum(counts.itervalues()) == 100000 )
  uniquenums = set(counts)
  return counts

def read_edit1s():
  """
  Returns the edit1s data
  It's a list of tuples, structured as [ .. , (misspelled query, correct query), .. ]
  """
  edit1s = []
  with open(edit1s_loc) as f:
    # the .rstrip() is needed to remove the \n that is stupidly included in the line
    edit1s = [ line.rstrip().split('\t') for line in f if line.rstrip() ]
  return edit1s

def serialize_data(data, fname):
  """
  Writes `data` to a file named `fname`
  """
  with open(fname, 'wb') as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

def unserialize_data(fname):
  """
  Reads a pickled data structure from a file named `fname` and returns it
  IMPORTANT: Only call pickle.load( .. ) on a file that was written to using pickle.dump( .. )
  """
  with open(fname, 'rb') as f:
    return pickle.load(f)

if __name__ == '__main__':
  print(sys.argv)
