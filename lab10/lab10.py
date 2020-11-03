# Author: Emily Hamrick eeh5387@psu.edu
# Collaborator: Alex Koretke ajk6357@psu.edu
# Collaborator: Purushottam Shukla pps5338@psu.edu
# Collaborator:
# Section: 3
# Breakout: 6

def remove_duplicate_sorted(t):
  """
  this function returns a new list generated from t that has t's
  elements without duplicates and is sorted from smallest to largest.
  """
  return set(t)

def list_to_dictionary(t):
  """
  t is a list of values (values could be str, list, tuple, set, dictionary),
  create and return a dictionary such that the key is len(v) for some v in t,
  and the value is a list of values [v1, v2, ...] from t (in the order they
  appeared in t) whose len(vi) is the key.
  for example: if t = [(1,2,3), "abc", [1, 2], (), ""]
  then return value of this function should be:
  {3: [(1, 2, 3), 'abc'], 2: [[1, 2]], 0: [(), '']}
  """
  d = dict()
  for i in t:
    if(len(i) not in d):
      d[len(i)] = i
    else:
      d[len(i)].add(i)
  return d

def run():
  """
  This function repeatedly ask user to enter a string and store them in a
  list and print it out.
  It also passes this list to remove_duplicate_sorted() function and
  list_to_dictionary() function and print out the results of the function
  calls.
  """
  values = []
  string = input("Enter a string: ")
  while(string != "done"):
    values.append(string)
    string = input("Enter a string: ")
  sortedv = remove_duplicate_sorted(values)
  dictv = list_to_dictionary(values)
  print(f"List: {values}" )
  print(f"Sorted List: {sortedv}")
  print(f"Dict: {dictv}")

if __name__ == "__main__":
  run()
