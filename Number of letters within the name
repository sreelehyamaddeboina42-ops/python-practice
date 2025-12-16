#Letters within the Name

user_name = input("Enter your name: ")
target_letter = input("Enter the letter for search: ")
count = 0
for letter in user_name:
    if letter == target_letter:
        count += 1
print(f"the letter '{target_letter}' appears {count} times in the name '{user_name}'")

#Advanced
user_name = input("Enter your name: ")
result = ""  

for letter in user_name:
    if letter in result: 
        continue
    count = user_name.count(letter) 
    result += letter + str(count)

print(result)
