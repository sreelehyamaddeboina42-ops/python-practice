Value = int(input("Enter a value: "))
input_value = Value 
temp_value = 0
reversed_value = 0
while Value > 0:
    temp_value = Value % 10
    reversed_value = (reversed_value * 10) + temp_value
    Value = Value // 10

print(reversed_value)
if input_value == reversed_value:
    print("The value is a palindrome.")
else:   
    print("The value is not a palindrome.")    


