# Given: 
# A string s of length at most 200 letters and four integers a, b, c and d.
#
# Return: 
# The slice of this string from indices a through b and c through d (with space in between), inclusively. 
# In other words, we should include elements s[b]and s[d]in our slice.

input = open('rosalind_ini3.txt', 'r').read()
output = open('output.txt', 'w')

text, a, b, c, d = input.split()

a = int(a)
b = int(b)
c = int(c)
d = int(d)

slice_1 = text[a:b+1]
slice_2 = text[c:d+1]

output.write(slice_1 + ' ' + slice_2)
output.close()