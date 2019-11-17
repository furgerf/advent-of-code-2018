#!/usr/bin/env python

import re

import numpy as np

if __name__ == "__main__":
  with open("input") as fh:
    data = [line.rstrip() for line in fh.readlines()]

  grid = np.zeros(shape=(1000, 1000))
  pattern = re.compile(r"\#(\S+) \@ (\d+),(\d+): (\d+)x(\d+)")
  for line in data:
    match = pattern.match(line)
    idx, x, y, width, height = match.groups()
    x = int(x)
    y = int(y)
    width = int(width)
    height = int(height)
    grid[x:x+width, y:y+height] += 1

  overlaps = np.where(grid > 1)
  print(len(overlaps[0]), len(overlaps[1]))

