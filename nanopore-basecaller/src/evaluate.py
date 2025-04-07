# Contents of /nanopore-basecaller/nanopore-basecaller/src/evaluate.py

import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader
from model import BasecallerModel  # Assuming the model is defined in model.py
from data_loader import load_data  # Assuming a function to load data is defined in data_loader.py
import matplotlib.pyplot as plt

def evaluate_model(model_path, test_data_path, batch_size=32):
    # Load the trained model
    model = BasecallerModel()
    model.load_state_dict(torch.load(model_path))
    model.eval()

    # Load test data
    test_data = load_data(test_data_path)
    test_loader = DataLoader(test_data, batch_size=batch_size, shuffle=False)

    all_predictions = []
    all_labels = []

    with torch.no_grad():
        for inputs, labels in test_loader:
            outputs = model(inputs)
            predictions = F.softmax(outputs, dim=1).argmax(dim=1)
            all_predictions.extend(predictions.numpy())
            all_labels.extend(labels.numpy())

    # Calculate accuracy
    accuracy = sum(np.array(all_predictions) == np.array(all_labels)) / len(all_labels)
    print(f'Accuracy: {accuracy * 100:.2f}%')

    # Visualize results
    plt.figure(figsize=(10, 5))
    plt.plot(all_labels, label='True Labels', alpha=0.5)
    plt.plot(all_predictions, label='Predictions', alpha=0.5)
    plt.title('Model Predictions vs True Labels')
    plt.xlabel('Sample Index')
    plt.ylabel('Label')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Evaluate the trained model.')
    parser.add_argument('--model', type=str, required=True, help='Path to the trained model file.')
    parser.add_argument('--test_data', type=str, required=True, help='Path to the test data file.')
    args = parser.parse_args()

    evaluate_model(args.model, args.test_data)