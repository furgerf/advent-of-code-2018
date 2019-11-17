#!/usr/bin/env python

if __name__ == "__main__":
  with open("input") as fh:
    data = fh.readlines()

  is_found = False
  found = set()
  counter = 0
  while not is_found:
    for d in data:
      counter += int(d)
      if counter in found:
        is_found = True
        print("Found", counter)
        break
      found.add(counter)

