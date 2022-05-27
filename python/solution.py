#!/usr/bin/python
def solution(nums, target):
  hashmap = {}

  for i, value in enumerate(nums):
    complement = target - value

    if complement in hashmap:
      return [hashmap[complement], i]

    hashmap[value] = i

print(solution([4, 3, 9, 10], 7)) # [0, 2]