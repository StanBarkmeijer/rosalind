# Given: 
# A DNA string s of length at most 1000 bp.
#
# Return: 
# The reverse complement sc of s.

input = open('rosalind_revc.txt', 'r').read().strip()
output = open('output.txt', 'w')

def reverse_complement(input):
    complement_object = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }

    complement = ""

    for i in input:
        complement += complement_object[i]

    return complement[::-1]

output.write(reverse_complement(input))