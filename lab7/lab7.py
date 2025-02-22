# Author: Emily Hamrick eeh5387@psu.edu
# Collaborator: Faraj Siddique fas5225@psu.edu
# Collaborator: Juliana Broadbent jfb5952@psu.edu
# Collaborator: Jacob Dally jed5801@psu.edu
# Section: 3
# Breakout: 12

import time
import itertools

def get_letters_combinations(alphabet, length):
  """
  Given an alphabet such as 'abcde', and a int length n such as 2,
  returns all n letter combinations from the alphabet in alphabetical
  order, such as ['ab','ac','ad','ae','bc','bd','be','cd','ce','de']
  """
  return list(map(''.join, itertools.combinations(alphabet, length)))

def uses_all(word, letters):
  """
  Return True if every letter in letters appeared in word;
  return False otherwise.
  """
  for c in letters:
    if c not in word:
      return False
  return True

def count_words_letters(words, letters):
  """
  Return the number of words in the list that used all letters in letters.
  """
  count = 0
  for word in words:
    if uses_all(word, letters):
      count += 1
  return count

def popular_letters(words, n):
  """
  Return the n letter combination from the alphabet such that
  all the letters in the combination appeared in the most number
  of words; if there are multiple combinations with the same
  popularity, return the combination that comes first in 
  alphabetic order.
  """
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  combinations = get_letters_combinations(alphabet, n)

  largest = combinations[0]
  occur = count_words_letters(words, largest)

  for combo in combinations[1:]:
    newoccur = count_words_letters(words, combo)
    if(newoccur > occur):
      occur = newoccur
      largest = combo
  return largest
  
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

def run():
  filename = input("Enter file name: ")
  words = get_words(filename)
  n = int(input("Enter an int: "))
  start = time.perf_counter()
  popular = popular_letters(words, n)
  end = time.perf_counter()
  print(f"{end-start} seconds to find popular {n}-letter combination:")
  print(f"Popular {n}-letter combination is: {popular}")

if __name__ == "__main__":
  run()
