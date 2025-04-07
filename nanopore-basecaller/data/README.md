# Data Structure for Nanopore Basecaller

This directory contains the data used for training and evaluating the Nanopore Basecaller model.

## Data Organization

### Raw Data
- The `raw` directory will contain raw `.fast5` files or simulated data. These files represent the electrical signals captured during the sequencing process.

### Processed Data
- The `processed` directory will hold preprocessed signal data along with labels, such as k-mers. This data is formatted and ready for use in training the machine learning model.

## Data Formats
- Raw data files are expected to be in the `.fast5` format, which is the standard output from Oxford Nanopore sequencing devices.
- Processed data will typically be stored in a structured format (e.g., CSV, JSON) that includes both the signal data and corresponding labels for supervised learning tasks.

Please ensure that the data is organized according to this structure to facilitate easy access and processing during model training and evaluation.