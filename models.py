
import sys
import os
import os.path

training_corpus_loc = './data/corpus/'
edit1s_loc = './data/edit1s.txt'

def scan_corpus():
  """
  Scans through the training corpus and counts how many lines of text there are
  """
  for sub_dir in os.listdir( training_corpus_loc ):
    print >> sys.stderr, 'processing dir: ' + sub_dir
    for fname in os.listdir( os.path.join( training_corpus_loc, sub_dir ) ):
      with open( os.path.join( training_corpus_loc, sub_dir, fname ) ) as f:
        num_lines = 0
        for line in f:
          # remember to remove the trailing \n
          line = line.rstrip()
          num_lines += 1
        print >> sys.stderr, 'Number of lines in ' + fname + ' is ' + str(num_lines)

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

if __name__ == '__main__':
  print(sys.argv)
