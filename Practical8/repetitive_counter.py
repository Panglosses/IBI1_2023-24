seq = "ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA"
n=0
for i in range(0,34):
    if seq[i:i+6]=="GTGTGT":
        n=n+1
    if seq[i:i+6]=="GTCTGT":
        n=n+1
    i=i+3
print(n)

