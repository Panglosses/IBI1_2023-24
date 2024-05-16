import blosum as bl

def read_fasta_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    seq_name = lines[0].split(' ')[1].strip()
    sequence = ''.join(line.strip() for line in lines[1:])
    return seq_name, sequence

def blosum62_score(seq1, seq2, blosum62_matrix):
    score = 0
    for aa1, aa2 in zip(seq1, seq2):
        score += blosum62_matrix.get(aa1, {}).get(aa2, 0)
    return score

def calculate_identity(seq1, seq2):
    return sum(aa1 == aa2 for aa1, aa2 in zip(seq1, seq2)) / len(seq1)

def compare_two_sequences(seq1_path, seq2_path, blosum62_matrix):
    seq1_name, seq1 = read_fasta_file(seq1_path)
    seq2_name, seq2 = read_fasta_file(seq2_path)
    score = blosum62_score(seq1, seq2, blosum62_matrix)
    identity = calculate_identity(seq1, seq2)
    return seq1_name, seq2_name, score, identity

def main():
    blosum62_matrix = bl.BLOSUM(62)
    
    human_seq_path = r'c:\Users\lhx\Desktop\IBI1\IBI1_2023-24\Practical13\SLC6A4_HUMAN.fa'
    mouse_seq_path = r'c:\Users\lhx\Desktop\IBI1\IBI1_2023-24\Practical13\SLC6A4_MOUSE.fa'
    rat_seq_path = r'c:\Users\lhx\Desktop\IBI1\IBI1_2023-24\Practical13\SLC6A4_RAT.fa'
    
    comparisons = [
        (human_seq_path, mouse_seq_path, 'Human', 'Mouse'),
        (human_seq_path, rat_seq_path, 'Human', 'Rat'),
        (mouse_seq_path, rat_seq_path, 'Mouse', 'Rat')
    ]
    
    results = []
    for seq1_path, seq2_path, name1, name2 in comparisons:
        seq1_name, seq2_name, score, identity = compare_two_sequences(seq1_path, seq2_path, blosum62_matrix)
        results.append((name1, name2, score, identity))  
    for name1, name2, score, identity in results:
        print(f"Alignment between {name1} and {name2}:")
        print(f"BLOSUM62 Score: {score}")
        print(f"Percentage Identity: {identity:.2%}\n")
    
    if results:  
        closest_results = max(results, key=lambda x: x[3])
        print(f"The sequences of {closest_results[0]} and {closest_results[1]} are most closely related with a BLOSUM62 score of {closest_results[2]} and {closest_results[3]:.2%} identity.")
        
        rodent_names = {'Mouse', 'Rat'}
        rodent_results = [result for result in results if result[0] in rodent_names or result[1] in rodent_names]
        if rodent_results: 
            better_rodent = min(rodent_results, key=lambda x: (-x[2], -x[3]))
            print(f"Based on the data analysed here, the {better_rodent[0]} is a better model organism for human.")
        else:
            print("No rodent species were found in the comparison results.")

if __name__ == "__main__":
    main()