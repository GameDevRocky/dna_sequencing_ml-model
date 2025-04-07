# Nanopore Basecaller with PyTorch 

This project explores how to translate raw electrical signal data from Oxford Nanopore sequencing into DNA k-mer sequences using machine learning.

## Project Structure
```
nanopore-basecaller
├── data
│   ├── raw
│   ├── processed
│   └── README.md
├── notebooks
│   └── exploratory_analysis.ipynb
├── src
│   ├── __init__.py
│   ├── data_loader.py
│   ├── model.py
│   ├── train.py
│   └── evaluate.py
├── tests
│   ├── __init__.py
│   ├── test_data_loader.py
│   ├── test_model.py
│   └── test_train.py
├── scripts
│   ├── preprocess_data.py
│   └── generate_synthetic_data.py
├── config.yaml
├── requirements.txt
└── README.md
```

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
```

## Data Structure
- **data/raw/**: Contains raw .fast5 files or simulated data.
- **data/processed/**: Holds preprocessed signal data along with labels, such as k-mers.

## Notebooks
- **notebooks/exploratory_analysis.ipynb**: Jupyter notebook for exploratory data analysis and experiments.

## Scripts
- **scripts/preprocess_data.py**: Script for preprocessing raw data into a format suitable for training.
- **scripts/generate_synthetic_data.py**: Script for generating synthetic data for testing and training purposes.

## Configuration
- **config.yaml**: Configuration settings for training, such as learning rate and batch size.

## Testing
- Unit tests are provided in the **tests/** directory to ensure the functionality of data loading, model definitions, and training processes.