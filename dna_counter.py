# dna_counter.py

def count_bases(dna_sequence):
    dna_sequence = dna_sequence.upper()
    base_counts = {
        'A': dna_sequence.count('A'),
        'T': dna_sequence.count('T'),
        'G': dna_sequence.count('G'),
        'C': dna_sequence.count('C')
    }
    return base_counts

# Example usage
sequence = input("Enter a DNA sequence (e.g., ATGCGTA): ")
counts = count_bases(sequence)

print("\nBase Counts:")
for base, count in counts.items():
    print(f"{base}: {count}")
