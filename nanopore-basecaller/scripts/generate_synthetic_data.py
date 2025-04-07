import numpy as np
import os

def generate_synthetic_data(num_samples=1000, sequence_length=100):
    """Generate synthetic DNA sequences and corresponding k-mer labels."""
    bases = ['A', 'C', 'G', 'T']
    synthetic_data = []
    labels = []

    for _ in range(num_samples):
        # Generate a random DNA sequence
        sequence = ''.join(np.random.choice(bases, sequence_length))
        synthetic_data.append(sequence)

        # Generate k-mers (for k=5 as an example)
        k = 5
        k_mers = [sequence[i:i+k] for i in range(len(sequence) - k + 1)]
        labels.append(k_mers)

    return synthetic_data, labels

def save_synthetic_data(data, labels, output_dir='data/processed'):
    """Save the generated synthetic data and labels to the specified directory."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    data_file = os.path.join(output_dir, 'synthetic_data.txt')
    labels_file = os.path.join(output_dir, 'synthetic_labels.txt')

    with open(data_file, 'w') as df:
        for sequence in data:
            df.write(f"{sequence}\n")

    with open(labels_file, 'w') as lf:
        for k_mers in labels:
            lf.write(','.join(k_mers) + '\n')

if __name__ == "__main__":
    synthetic_data, labels = generate_synthetic_data()
    save_synthetic_data(synthetic_data, labels)