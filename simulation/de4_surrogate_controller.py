import torch, torch.nn as nn

class DE4Surrogate(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(6, 32),
            nn.Tanh(),
            nn.Linear(32, 32),
            nn.Tanh(),
            nn.Linear(32, 3)
        )
    def forward(self, x):
        return self.net(x)

def run_mpc(config):
    steps = 200
    log_true, log_sur = [], []
    surrogate = DE4Surrogate()
    for t in range(steps):
        state = torch.randn(6)
        true = torch.sin(state.sum()) * 0.5
        pred = surrogate(state).sum().item() * 0.5
        log_true.append({'torque': true, 'loss': abs(true)/5, 'utility': true - abs(true)/5})
        log_sur.append({'torque': pred, 'loss': abs(pred)/5, 'utility': pred - abs(pred)/5})
    return log_true, log_sur
