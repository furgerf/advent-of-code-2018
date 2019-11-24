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

def part_1(data):
  print("Running part 1")

  max_guard = data.keys()[0]
  max_sleep = sum([s[2] for s in data[max_guard]])
  for guard, sleep in data.items():
    current_sleep = sum([s[2] for s in sleep])
    if current_sleep > max_sleep:
      max_guard = guard
      max_sleep = current_sleep

  print(max_guard, max_sleep)
  minutes = np.zeros(60)
  for sleep_start, sleep_end, _ in data[max_guard]:
    minutes[sleep_start:sleep_end] += 1

  index = np.argmax(minutes)
  print(max_guard, minutes, index, minutes[index], max_guard * index)

def part_2(data):
  print("Running part 2")

  max_count = -1
  max_guard = None
  max_minute = None
  for guard in data:
    minutes = np.zeros(60)
    for sleep_start, sleep_end, _ in data[guard]:
      minutes[sleep_start:sleep_end] += 1
    if max(minutes) > max_count:
      max_count = max(minutes)
      max_guard = guard
      max_minute = np.argmax(minutes)

  print(max_count, max_guard, max_minute, max_guard * max_minute)

def load_data():
  file_name = os.path.join(os.path.dirname(__file__), "input")
  with open(file_name) as fh:
    return [line.rstrip() for line in fh.readlines()]

def parse_data(raw_data):
  parsed_data = []
  for line in raw_data:
    split = line.split(" ")
    date_part = " ".join(split[:2])[1:-1]
    action_part = split[2:]

    date = datetime.strptime(date_part, "%Y-%m-%d %H:%M")
    info = action_part[1][1:] if action_part[0] == "Guard" else action_part[0]
    parsed_data.append((date, info))

  data = sorted(parsed_data, key=lambda x: x[0])

  sleep_times = {}
  guard = None
  sleep_start = None
  for date, entry in data:
    if entry == "falls":
      assert not sleep_start
      sleep_start = date
    elif entry == "wakes":
      assert sleep_start and guard
      if not guard in sleep_times:
        sleep_times[guard] = []
      sleep_times[guard].append((sleep_start.minute, date.minute, (date - sleep_start).seconds // 60))
      sleep_start = None
    else:
      assert not sleep_start
      guard = int(entry)

  return sleep_times

def main():
  args = parse_arguments()
  data = parse_data(load_data())

  if args.part_1:
    part_1(data)

  if args.part_2:
    part_2(data)

  return

if __name__ == "__main__":
  main()
