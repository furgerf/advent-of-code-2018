#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
from argparse import ArgumentParser
from datetime import datetime

import numpy as np


def parse_arguments():
  parser = ArgumentParser()

  parser.add_argument("-1", "--part-1", action="store_true")
  parser.add_argument("-2", "--part-2", action="store_true")
  parser.add_argument("--fabian", action="store_true")

  return parser.parse_args()

def part_1_corinne(data):
  print("Running part 1 à la Corinne")

  min_x = min([d[0] for d in data])
  min_y = min([d[1] for d in data])

  data[:, 0] -= min_x
  data[:, 1] -= min_y
  max_x = max([d[0] for d in data])
  max_y = max([d[1] for d in data])

  grid = np.full((max_x, max_y), -1)

  def get_closest_point(index):
    min_distance = max_x + max_y
    closest_point = None

    for i, point in enumerate(data):
      distance = abs(point[0] - index[0]) + abs(point[1] - index[1])
      if distance < min_distance:
        min_distance = distance
        closest_point = i
      elif distance == min_distance:
        closest_point = -1

    return closest_point

  for index, _ in np.ndenumerate(grid):
    grid[index] = get_closest_point(index)

  print(grid)

  border = set(grid[0]).union(set(grid[:, 0])).union(set(grid[-1])).union(set(grid[:, -1]))

  print(border)
  max_index = None
  max_area = 0
  for i in range(len(data)):
    if i in border:
      continue
    area_size = len(np.where(grid == i)[0])
    if area_size > max_area:
      max_area = area_size
      max_index = i

  print(max_index, max_area)

def part_1_fabian(data):
  print("Running part 1 à la Fabian")

  min_x = min([d[0] for d in data])
  min_y = min([d[1] for d in data])
  data[:, 0] -= min_x
  data[:, 1] -= min_y
  max_x = max([d[0] for d in data])
  max_y = max([d[1] for d in data])

  def get_closest_point(index):
    min_distance = max_x + max_y
    closest_point = None

    for i, point in enumerate(data):
      distance = abs(point[0] - index[0]) + abs(point[1] - index[1])
      if distance < min_distance:
        min_distance = distance
        closest_point = i
      elif distance == min_distance:
        closest_point = -1

    return closest_point

  def add_neighbors(point, neighbors, visited):
    for dx in [-1, 1]:
      if point[0] + dx < 0 or point[0] + dx >= max_x:
        return False
      current_point = (point[0] + dx, point[1])
      if current_point not in visited:
        neighbors.add(current_point)
        visited.add(current_point)
    for dy in [-1, 1]:
      if point[1] + dy < 0 or point[1] + dy >= max_y:
        return False
      current_point = (point[0], point[1] + dy)
      if current_point not in visited:
        neighbors.add(current_point)
        visited.add(current_point)
    return True

  max_index = None
  max_area = 0
  print(max_x, max_y)
  for i, point in enumerate(data):
    visited = set(point)
    neighbors = set()
    area_size = 0
    if not add_neighbors(point, neighbors, visited):
      continue

    while neighbors:
      neighbor = neighbors.pop()
      closest_index = get_closest_point(neighbor)
      if closest_index != i:
        continue
      area_size += 1
      add_neighbors(neighbor, neighbors, visited)

    if area_size > max_area:
      max_index = i
      max_area = area_size

  print(max_index, max_area)

def part_2(data):
  print("Running part 2")

  MAX_DISTANCE = 10000

  min_x = min([d[0] for d in data])
  min_y = min([d[1] for d in data])
  max_x = max([d[0] for d in data])
  max_y = max([d[1] for d in data])

  in_range = 0
  for i in range(min_x, max_x+1):
    for j in range(min_y, max_y+1):
      distance = 0
      for point in data:
        distance += abs(point[0] - i) + abs(point[1] - j)
      if distance <= MAX_DISTANCE:
        in_range += 1
  print(in_range)

def load_data():
  file_name = os.path.join(os.path.dirname(__file__), "input")
  with open(file_name) as fh:
    return [line.rstrip() for line in fh.readlines()]

def parse_data(raw_data):
  parsed_data = []
  for line in raw_data:
    parsed_data.append([int(i) for i in line.split(", ")])

  return np.array(parsed_data)

def main():
  args = parse_arguments()
  data = parse_data(load_data())

  if args.part_1:
    if args.fabian:
      part_1_fabian(data)
    else:
      part_1_corinne(data)

  if args.part_2:
    part_2(data)

  return

if __name__ == "__main__":
  main()
