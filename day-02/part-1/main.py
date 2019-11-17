#!/usr/bin/env python

if __name__ == "__main__":
  with open("input") as fh:
    data = fh.readlines()

  two_letters = 0
  three_letters = 0

  for d in data:
    counts = {}
    for char in d:
      if char not in counts:
        counts[char] = 0
      counts[char] += 1

    if 2 in counts.values():
      two_letters += 1
    if 3 in counts.values():
      three_letters += 1

  print("Two", two_letters, "Three", three_letters, "Product", two_letters*three_letters)

