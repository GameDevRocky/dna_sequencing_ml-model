class BasecallerModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(BasecallerModel, self).__init__()
        self.rnn = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out, _ = self.rnn(x)
        out = self.fc(out[:, -1, :])  # Get the last time step
        return out

def create_model(config):
    input_size = config['model']['input_size']
    hidden_size = config['model']['hidden_size']
    output_size = config['model']['output_size']
    model = BasecallerModel(input_size, hidden_size, output_size)
    return model