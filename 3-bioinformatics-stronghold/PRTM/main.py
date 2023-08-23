# Given: 
# A protein string P of length at most 1000 aa.
# 
# Return: 
# The total weight of P . 
# Consult the monoisotopic mass table.

input = open("rosalind_prtm.txt", "r").read().strip()
output = open("output.txt", "w")

monoisotopic_mass_string = "A   71.0371\nC   103.00919\nD   115.02694\nE   129.04259\nF   147.06841\nG   57.02146\nH   137.05891\nI   113.08406\nK   128.09496\nL   113.08406\nM   131.04049\nN   114.04293\nP   97.05276\nQ   128.05858\nR   156.10111\nS   87.03203\nT   101.04768\nV   99.06841\nW   186.07931\nY   163.06333"
monoisotopic_mass_table = monoisotopic_mass_string.split("\n")
monoisotopic_mass_table = [line.split() for line in monoisotopic_mass_table]
monoisotopic_mass_table = {line[0]: float(line[1]) for line in monoisotopic_mass_table}

def calculate_protein_weight(protein):
    weight = 0

    for aa in protein:
        weight += monoisotopic_mass_table[aa]
    
    return round(weight, 3)

output.write(str(calculate_protein_weight(input)))
output.close()