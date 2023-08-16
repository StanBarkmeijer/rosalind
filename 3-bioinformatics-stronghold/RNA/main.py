# Given: 
# A DNA string t having length at most 1000 nt.
#
# Return: 
# The transcribed RNA string of t.

input = open("rosalind_rna.txt", "r").read().strip()
output = open("output.txt", "w")

dict = {
    "A": "A",
    "T": "U",
    "C": "C",
    "G": "G",
}

output.write("".join([dict[i] for i in input]))
output.close()