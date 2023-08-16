# Given: 
# Two positive integers a and b (a < b < 10000).
#
# Return: 
# The sum of all odd integers from a through b, inclusively.

input = open('rosalind_ini4.txt', 'r').read()
output = open('output.txt', 'w')

a, b = map(int, input.split())

sum = 0

for i in range(a, b+1):
    if i % 2 != 0:
        sum += i

output.write(str(sum))
output.close()