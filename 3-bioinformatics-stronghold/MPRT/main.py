import re
import requests

input = open("rosalind_mprt.txt", "r").read()
output = open("output.txt", "w")

input = input.split("\n")

def find_motif(fasta_string):
    motif = re.finditer(r"(?=N[^P][ST][^P])", fasta_string)
    motif = [str(m.start() + 1) for m in motif]

    return motif

for protein_id in input:
    prt_string = protein_id

    if "_" in protein_id:
        protein_id = protein_id.split("_")[0]

    url = "http://www.uniprot.org/uniprot/" + protein_id + ".fasta"
    
    fasta = requests.get(url).text    
    fasta = fasta.split("\n")
    fasta.pop(0)
    fasta = "".join(fasta)
    
    motif = find_motif(fasta)

    if len(motif) > 0:
        print(prt_string)
        print(" ".join(motif))
        output.write(prt_string + "\n" + " ".join(motif) + "\n")

output.close()