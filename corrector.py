
import sys

queries_loc = 'data/queries.txt'
gold_loc = 'data/gold.txt'
google_loc = 'data/google.txt'

alphabet = "abcdefghijklmnopqrstuvwxyz0123546789&$+_' "

def read_query_data():
  """
  all three files match with corresponding queries on each line
  """
  queries = []
  correct = []
  google = []
  with open(queries_loc) as f:
    for line in f:
      queries.append(line.rstrip())
  with open(gold_loc) as f:
    for line in f:
      correct.append(line.rstrip())
  with open(google_loc) as f:
    for line in f:
      google.append(line.rstrip())
  assert( len(queries) == len(correct) and len(correct) == len(google) )
  return (queries, correct, google)

if __name__ == '__main__':
  print(sys.argv)
