# Given: 
# A DNA string s of length at most 1000 nt.
#
# Return: 
# Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

input = open("rosalind_dna.txt", "r").read().strip().lower().replace("\n", "")
input = list(input)
output = open("output.txt", "w")

nucleotides = ["a", "c", "g", "t"]
text = ""

for n in nucleotides:
    text += str(input.count(n)) + " "

output.write(text)
output.close()