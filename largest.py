I = int(input("Enter the first number: "))
II = int(input("Enter the second number: "))
III = int(input("Enter the third number: "))
if I > II and I > III:
    print("The largest number is:", I)
elif II > I and II > III:
    print("The largest number is:", II)
else:    print("The largest number is:", III)