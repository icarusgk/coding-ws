from collections import defaultdict

dogs = ["pomeranian", "labrador", "corgi", "corgi", "golden retriever", "corgi", "labrador"]

dogs_dict = defaultdict(int)

for dog in dogs:
    dogs_dict[dog] += 1

print(dogs_dict["corgi"])
print(dogs_dict["husky"])
print(dogs_dict["poodle"])

print(dogs_dict)