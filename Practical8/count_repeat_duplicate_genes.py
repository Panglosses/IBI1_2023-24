import re
from Bio import SeqIO

repetitive_sequence = input("Enter the repetitive sequence (GTGTGT or GTCTGT): ")

output_filename = f"{repetitive_sequence}_duplicate_genes.fa"

duplicate_genes = []

input_filename = "c:/Users/lhx/Desktop/IBI1/IBI1_2023-24/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
with open(input_filename, "r") as input_file:
    for record in SeqIO.parse(input_file, "fasta"):
        sequence = str(record.seq).replace("\n", "")
        if re.search(repetitive_sequence, sequence):
            gene_name = re.search(r"\b(\w+)\b", record.description).group(1)
            duplicate_genes.append((gene_name, sequence))

with open(output_filename, "w") as output_file:
    for gene_name, sequence in duplicate_genes:
        output_file.write(f">{gene_name} {sequence.count(repetitive_sequence)}\n{sequence}\n")

print(f"Duplicate genes containing {repetitive_sequence} saved in {output_filename}")