#!/usr/bin/env python

import numpy as np

if __name__ == "__main__":
  with open("input") as fh:
    data = [line.rstrip() for line in fh.readlines()]

  for i, d in enumerate(data):
    for dd in data[:i]:
      assert len(d) == len(dd)
      differences = []
      for j in range(len(d)):
        if d[j] != dd[j]:
          differences.append(j)
        if len(differences) > 1:
          break
      if len(differences) == 1:
        print(d)
        print(dd)
        remaining = list(sorted(set(range(len(d))) - set(differences)))
        print(differences, remaining)
        print("".join(np.array([char for char in d])[remaining]))

        assert False

