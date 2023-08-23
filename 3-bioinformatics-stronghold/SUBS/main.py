# Given: 
# Two DNA strings s and t (each of length at most 1 kbp).
#
# Return: 
# All locations of t as a substring of s.

input = open("rosalind_subs.txt", "r").read().strip()
output = open("output.txt", "w")

s, t = input.split("\n")

def find_motif(s, t):
    locations = []

    for i in range(len(s)):
        if s[i:].startswith(t):
            locations.append(i + 1)

    return locations

output.write(" ".join(map(str, find_motif(s, t))))
output.close()