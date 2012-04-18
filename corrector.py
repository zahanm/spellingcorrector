
import sys

queries_loc = './data/dev/queries.txt'
gold_loc = './data/dev/gold.txt'

alphabet = "abcdefghijklmnopqrstuvwxyz0123546789&$+_' "

def read_query_data():
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
