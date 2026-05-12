character = (input('Enter a Word/Statement:'))
count = 0

for ch in character.lower():
    if ch in "aieou":
        count+=1
print('Number of Vowels are =', count)
 #just for future ref
# the 'ch' stores one letter at a time