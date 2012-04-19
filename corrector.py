
import sys

queries_loc = './data/queries.txt'
gold_loc = './data/gold.txt'

alphabet = "abcdefghijklmnopqrstuvwxyz0123546789&$+_' "

def read_query_data():
  """
  both files match with corresponding queries on each line
  the data/gold.txt file has results in the format
  [ .. , (correct, google), .. ]
  """
  queries = []
  correct = []
  google = []
  with open(queries_loc) as f:
    for line in f:
      queries.append(line.rstrip())
  with open(gold_loc) as f:
    for line in f:
      a, b = line.rstrip().split('\t')
      correct.append(a)
      google.append(b)
  assert( len(queries) == len(correct) and len(correct) == len(google) )
  return (queries, correct, google)

if __name__ == '__main__':
  print(sys.argv)
