nums = {"one": 1, "two": 2, "three": 3}


for num in nums.keys():
  print(f"Number for {num}:")
  n = int(input())

  if nums[num] == n:
    print("correct")
  elif n in nums.values():
    print(f"{n} is correct for {list(nums.keys())[list(nums.values()).index(n)]}")
    # mydict.keys()[mydict.values().index(16)]

