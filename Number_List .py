# 1. Number List Builder
Numbers = int(input("How many Numbers do you want: "))
Numbers_list = []   
for number in range(0,Numbers):
    value = int(input("Enter Number: "))
    Numbers_list.append(value)
print(f"the numbers you have entered are {Numbers_list}")
sum = 0
for number in Numbers_list:
    sum += number
print(f"The sum of the numbers you have entered is {sum}")

average = 0
for number in Numbers_list:
    average = sum/Numbers
print(f"The average of the numbers you have entered is {average}")
Maximum = 0
for number in Numbers_list:
    if number > Maximum:
        Maximum = number
print(f"The Maximum of the numbers you have entered is {Maximum}")

Minimum = Numbers_list[0]
for number in Numbers_list:
    if number < Minimum:
        Minimum = number
print(f"The Minimum of the numbers you have entered is {Minimum}")