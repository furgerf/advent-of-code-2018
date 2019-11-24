#!/usr/bin/env python

import os
import re
from argparse import ArgumentParser
from datetime import datetime

import numpy as np


def parse_arguments():
  parser = ArgumentParser()

  parser.add_argument("-1", "--part-1", action="store_true")
  parser.add_argument("-2", "--part-2", action="store_true")

  return parser.parse_args()

def reduce_polymer(data):
  def are_reducible(a, b):
    return abs(ord(a) - ord(b)) == 32 # ord("a") - ord("A")

  cursor = 0
  while cursor < len(data)-1:
    if are_reducible(data[cursor], data[cursor+1]):
      del data[cursor+1]
      del data[cursor]
      if cursor > 0:
        cursor -= 1
    else:
      cursor += 1

  return len(data)

def part_1(data):
  print("Running part 1")
  print(reduce_polymer(data))

def part_2(data):
  print("Running part 2")

  shortest_length = len(data)
  for character in range(ord("a"), ord("z")):
    shortened_data = [d for d in data if ord(d.lower()) != character]
    current_length = reduce_polymer(shortened_data)
    if current_length < shortest_length:
      shortest_length = current_length

  print(shortest_length)

def load_data():
  file_name = os.path.join(os.path.dirname(__file__), "input")
  with open(file_name) as fh:
    return [c for c in fh.readline()]

def main():
  args = parse_arguments()
  data = load_data()

  if args.part_1:
    part_1(data)

  if args.part_2:
    part_2(data)

  return

if __name__ == "__main__":
  main()
