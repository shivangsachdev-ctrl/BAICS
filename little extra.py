character = input('Enter the Word:')
count = 0

for ch in character.lower():
    if ch in "aieou":
        count +=1
print('The Number Of Vowels =', count)

f = int(input('Find Factorial of this number?: (1 is yes, 0 is no)'))

if f==1:
    n = count
    factorial = 1

    for i in range(1,n+1):
        factorial *= i
    print('The Factorial of this Number is =', factorial)
else: print('Thank You')


count = 0
p = int(input('Find Prime Numbers?: (1 is yes, 0 is no)'))
if p == 1:

        for ch in range(1,factorial):
            is_prime = 1
            for n in range(2,ch):
                if ch % n == 0:
                 is_prime = 0
                 break
            if is_prime==1:
             count +=1
else: print('Thank you')

           
           
print('The Number of prime numbers between 0 and factorial is =', count)

A = int(input('Find Area of circle with this Number?: (1 is yes, 0 is no)'))
if A==1:
            print((count)**2 * 3.14)
else:
            print('Thank You')
    
        