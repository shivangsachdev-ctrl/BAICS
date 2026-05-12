numbers = input('Enter a list of numbers')

new_list = []

for value in numbers:
    if value not in new_list:
        new_list.append(value)

print("List after removing duplicates:", new_list)