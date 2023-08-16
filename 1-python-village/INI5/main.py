# Given: 
# A file containing at most 1000 lines.
#
# Return: 
# A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

input = open('rosalind_ini5.txt', 'r').read().splitlines()

output = open('output.txt', 'w')

for i in range(1, len(input), 2):
    output.write(input[i] + '\n')

output.close()