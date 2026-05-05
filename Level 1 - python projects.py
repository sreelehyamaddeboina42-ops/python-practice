# 1. Even or Odd Number
Number = int(input("Enter a number: "))

if Number%2 == 0:
    print("This is a Even number")
        
else:
    print("This is a Odd number")

    
# 2. Print the first x natural numbers
x = int(input("Enter a Number: "))

for i in range(0,x):
    print(i + 1)

    
# 3. Countdown Timer
time = int(input("Enter the time in seconds: "))

for x in range(time, -1, -1):
    print(x) 
