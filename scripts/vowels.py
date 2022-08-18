# counts the number of vowels in a txt file
import os

with open('vowels.txt', 'r') as f:
    vowels = 0
    for line in f:
        for char in line:
            if char in 'aeiou':
                vowels += 1
    print(vowels)

os.rename('vowels.txt', 'vowels + ' + '-' + str(vowels) + '.txt')