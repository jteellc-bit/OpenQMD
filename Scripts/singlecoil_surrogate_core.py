import torch
import torch.nn as nn

class SingleCoilSurrogate(nn.Module):
    def __init__(self, in_dim=3, hidden=48, out_dim=3):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden),
            nn.ReLU(),
            nn.Linear(hidden, hidden),
            nn.ReLU(),
            nn.Linear(hidden, out_dim)
        )
    def forward(self, x):
        return self.net(x)

def save_model(path):
    model = SingleCoilSurrogate()
    torch.save(model.state_dict(), path)
