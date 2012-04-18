
import sys
import cPickle as pickle

training_corpus_loc = './data/corpus/'
edit1s_loc = './data/edit1s.txt'

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
