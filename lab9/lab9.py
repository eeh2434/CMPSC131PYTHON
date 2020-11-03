# Author: Emily Hamrick eeh5387@psu.edu
# Collaborator: Sara Preller skp5565@psu.edu
# Collaborator: Andrew Torri abt5506@psu.edu
# Collaborator: Faraj Siddique fas5225@psu.edu
# Section: 3
# Breakout: 5
from sys import argv
def get_words(filename):
  """
  Given a filename (as a str), open the file and retrieve words from
  each line to create a list with whitespaces stripped.
  """
  ans = []
  with open(filename) as fin:
    for line in fin:
      ans.append(line.strip())
  return ans

def invert_dict(d):
  """
  Given a dictionary d, create the invert of the dictionary where
  the key is a value v in d, and v is mapped to a set of keys in original
  d whose values are equal to v.
  Return the inverted dictionary mapping value to set of keys
  """
  dinvert = dict()
  for key in d:
    newk = d[key]
    if(newk not in dinvert):
      dinvert[newk] = {key}
    else:
      dinvert[newk].add(key)
  return dinvert

def histogram(words):
  """
  Given a list of words, create a histogram dictionary where the key
  is the length of a word and the value is the count of how many
  words in the list are of that length.
  Return the histogram dictionary mapping length to word counts
  """
  histo = dict()
  for w in words:
    if(len(w) not in histo):
      histo[len(w)] = 1
    else:
      histo[len(w)] += 1
  return histo 

def max_kv(d):
  """
  Given a dictionary, return a tuple of key value pair where the key
  is the largest in d.
  """
  maxk = max(d)
  return maxk, d[maxk]

def run():
  """
  Get words list from the file listed in argv[1];
  create histogram of count of each word length;
  create invert dictionary that maps count to list of word length;
  use invert dictionary to find the list of word length with the
  most popular word count (use max_kv)
  """
  words = get_words(argv[1])
  # fill in code here
  histow = histogram(words)
  inverseh = invert_dict(histow)
  # modify the line below so that count, length_set has the right values
  count, length_set = max_kv(inverseh)
  print(f"These word length {length_set} each has {count} words.") 

if __name__ == "__main__":
  run()
