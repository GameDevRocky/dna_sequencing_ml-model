import pytest
from src.train import train_model

def test_train_model():
    # Mock data and parameters for testing
    mock_data = {
        'input': [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]],
        'labels': [0, 1]
    }
    mock_config = {
        'learning_rate': 0.001,
        'epochs': 5,
        'batch_size': 2
    }
    
    # Call the training function
    model, history = train_model(mock_data, mock_config)
    
    # Assertions to verify the model and training history
    assert model is not None, "Model should not be None"
    assert len(history) == mock_config['epochs'], "History should contain epochs"
    assert all(isinstance(loss, float) for loss in history), "Loss values should be floats"