numbers = [1, 2, 3, 4, 5]
numbers.extend([10, 20, 30])
print(numbers)  # [1, 2, 3, 4, 5, 10, 20, 30]

numbers = [1, 2, 3, 4, 5]
numbers.append([10, 20, 30])
print(numbers)  # [1, 2, 3, 4, 5, [10, 20, 30]]


numbers_to_four = [0, 1, 2, 3, 4]
numbers_from_five = [5, 6, 7, 8, 9]
numbers = numbers_to_four + numbers_from_five 
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

pattern = ['a', 'b', 'c']
patterns = pattern * 3
print(patterns)  # ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']

one = [1]
ones = one * 7
print(ones)  # [1, 1, 1, 1, 1, 1, 1]


dragons = ['Rudror', 'Targiss', 'Coporth', 'Targiss']
dragons.remove('Targiss')
print(dragons)  # ['Rudror', 'Coporth', 'Targiss']

dragons = ['Rudror', 'Targiss', 'Coporth']
del dragons[1]
print(dragons)  # ['Rudror', 'Coporth']

dragons = ['Rudror', 'Targiss', 'Coporth']
first_dragon = dragons.pop(0)
print(first_dragon)  # 'Rudror'
print(dragons)       # ['Targiss', 'Coporth']



years = [2016, 2018, 2019]
years.insert(1, 2017)           # [2016, 2017, 2018, 2019]
years.insert(0, 2015)           # [2015, 2016, 2017, 2018, 2019]
years.insert(len(years), 2020)  # [2015, 2016, 2017, 2018, 2019, 2020]



grades = [10, 5, 7, 9, 5, 10, 9]
print(grades.count(5))  # 2


print(grades.index(7))   # 2
print(grades.index(10))  # 0




def merge_lists(list_one, list_two):
    return list_one + list_two

print(merge_lists(['Washington, D.C.', 'Chicago', 'New York'], ['Los Angeles', 'Las Vegas']))