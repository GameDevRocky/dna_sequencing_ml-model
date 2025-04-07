# Contents of /nanopore-basecaller/nanopore-basecaller/src/train.py

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from data_loader import SignalDataset
from model import BasecallerModel
import yaml

def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def train_model(model, dataloader, criterion, optimizer, num_epochs):
    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0
        for inputs, labels in dataloader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {running_loss/len(dataloader):.4f}')

def main(config_path):
    config = load_config(config_path)
    
    # Initialize dataset and dataloader
    dataset = SignalDataset(config['data']['train_data'])
    dataloader = DataLoader(dataset, batch_size=config['training']['batch_size'], shuffle=True)
    
    # Initialize model, criterion, and optimizer
    model = BasecallerModel(config['model'])
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=config['training']['learning_rate'])
    
    # Train the model
    train_model(model, dataloader, criterion, optimizer, config['training']['num_epochs'])

if __name__ == '__main__':
    main('config.yaml')