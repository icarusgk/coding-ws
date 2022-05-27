input_list = []

for i in range(9):
    n = int(input("n: "))
    input_list.append(n)

print(input_list)

position = int(input("Enter the position of the number you want to see: "))
print(input_list[position])