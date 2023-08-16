# Given: 
# Two positive integers a and b, each less than 1000.
#
# Return: 
# The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.

input = open('rosalind_ini2.txt', 'r').read()
output = open('output.txt', 'w')

a, b = input.split(' ')

a = int(a)
b = int(b)

output.write(str(a**2 + b**2))
output.close()