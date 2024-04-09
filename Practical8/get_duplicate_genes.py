from Bio import SeqIO
input_file = "c:/Users/lhx/Desktop/IBI1/IBI1_2023-24/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "duplicate_genes.fa"
keyword = "duplication"

duplicate_genes = []

with open(input_file, "r") as f:
    for record in SeqIO.parse(f, "fasta"):
        if keyword in record.description:
            gene_name = record.id.split()[0]  
            duplicate_genes.append((gene_name, str(record.seq).replace("\n", "")))

with open(output_file, "w") as f:
    for gene_name, sequence in duplicate_genes:
        f.write(f">{gene_name}\n{sequence}\n")