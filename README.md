# Nanopore Basecaller with PyTorch 

This project explores how to translate raw electrical signal data from Oxford Nanopore sequencing into DNA k-mer sequences using machine learning.

## Features
- Synthetic & real squiggle data
- PyTorch-based k-mer classifier
- Modular pipeline
- Extensible to RNNs, Transformers

## Usage
```bash
# Install dependencies
pip install -r requirements.txt

# Train model on synthetic data
python src/train.py --config config.yaml

# Evaluate performance
python src/evaluate.py --model saved_model.pt
