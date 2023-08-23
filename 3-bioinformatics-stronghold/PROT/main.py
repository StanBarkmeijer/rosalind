# Given: 
# An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
#
# Return: 
# The protein string encoded by s

input = open("rosalind_prot.txt", "r").read().strip()
output = open("output.txt", "w")

rna_codon_string = "UUU F      CUU L      AUU I      GUU V\nUUC F      CUC L      AUC I      GUC V\nUUA L      CUA L      AUA I      GUA V\nUUG L      CUG L      AUG M      GUG V\nUCU S      CCU P      ACU T      GCU A\nUCC S      CCC P      ACC T      GCC A\nUCA S      CCA P      ACA T      GCA A\nUCG S      CCG P      ACG T      GCG A\nUAU Y      CAU H      AAU N      GAU D\nUAC Y      CAC H      AAC N      GAC D\nUAA Stop   CAA Q      AAA K      GAA E\nUAG Stop   CAG Q      AAG K      GAG E\nUGU C      CGU R      AGU S      GGU G\nUGC C      CGC R      AGC S      GGC G\nUGA Stop   CGA R      AGA R      GGA G\nUGG W      CGG R      AGG R      GGG G"
rna_codon_string = rna_codon_string.split()
rna_codon_dict = dict(zip(rna_codon_string[0::2], rna_codon_string[1::2]))

protein = "".join([rna_codon_dict[input[i:i+3]] for i in range(0, len(input), 3) if rna_codon_dict[input[i:i+3]] != "Stop"])

output.write(protein)
output.close()