# Given: 
# A string s of length at most 10000 letters.
#
# Return: 
# The number of occurrences of each word in s, where words are separated by spaces. 
# Words are case-sensitive, and the lines in the output can be in any order.

input = open('rosalind_ini6.txt', 'r').read().strip().split()
output = open('output.txt', 'w')

word_count = {}

for word in input:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word in word_count:
    output.write(word + ' ' + str(word_count[word]) + '\n')

output.close()