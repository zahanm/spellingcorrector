
import random
import itertools
import cPickle as pickle

from collections import Counter

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
  for i in xrange(10000):
    num = random.randint(0, 10)
    counts[ num ] += 1
  assert( sum(counts.itervalues()) == 10000 )
  uniquenums = set(counts)
  return counts

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
  print('Toy code')
  walk_pairs()
  print( count_ints() )
