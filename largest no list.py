numbers = (input('Enter  a list of numbers:'))

largest = numbers[0]

for value in numbers:
    if value > largest:
        largest = value

print("Largest number is:", largest)