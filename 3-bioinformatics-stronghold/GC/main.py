# Given: 
# At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
#
# Return: 
# The ID of the string having the highest GC-content, followed by the GC-content of that string. 
# Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

# input = ">Rosalind_6404\nCCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC\nTCCCACTAATAATTCTGAGG\n>Rosalind_5959\nCCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT\nATATCCATTTGTCAGCAGACACGC\n>Rosalind_0808\nCCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"
input = open("rosalind_gc.txt", "r").read()
output = open("rosalind_gc_out.txt", "w")

input = input.split(">")
input.pop(0)

def calculate_gc(dna):
    gc = 0

    for nucleotide in dna:
        if nucleotide == "G" or nucleotide == "C":
            gc += 1

    return round(gc / len(dna) * 100, 6)

dna_dict = {}

for dna_string in input:
    key = dna_string.split("\n")[0]
    value = "".join(dna_string.split("\n")[1:])

    dna_dict[key] = {
        "value": value,
        "gc": calculate_gc(value)
    }
   
    sorted_dna_dict = sorted(dna_dict.items(), key=lambda x: x[1]["gc"], reverse=True)

print(sorted_dna_dict[0][0] + "\n" + str(sorted_dna_dict[0][1]["gc"]))
output.write(sorted_dna_dict[0][0] + "\n" + str(sorted_dna_dict[0][1]["gc"]))
output.close()