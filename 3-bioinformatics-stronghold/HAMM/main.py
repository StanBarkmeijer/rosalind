# Given: 
# Two DNA strings s and t of equal length (not exceeding 1 kbp).
#
# Return: 
# The Hamming distance dH(s,t).

input = open("rosalind_hamm.txt", "r").read().strip().split("\n")
output = open("output.txt", "w")

s1, s2 = input[0], input[1]

def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Strings must be of equal length.")

    if s1 == s2:
        return 0

    distance = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1

    return distance

output.write(str(hamming_distance(s1, s2)))
output.close()