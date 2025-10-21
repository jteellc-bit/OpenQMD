
import torch, torch.nn as nn, torch.optim as optim
import numpy as np, matplotlib.pyplot as plt, json, os

class DE4Surrogate3x3(nn.Module):
    def __init__(self, n_in=3, n_out=3, hidden=32):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_in, hidden), nn.Tanh(),
            nn.Linear(hidden, hidden), nn.Tanh(),
            nn.Linear(hidden, n_out)
        )
    def forward(self, x): return self.net(x)

def gen_synthetic_data(n=2000):
    x = np.random.uniform(-1, 1, (n, 3))
    torque = np.sin(2*np.pi*x[:,0]) + 0.3*np.cos(2*np.pi*x[:,1]) - 0.2*x[:,2]
    loss = 0.1 + 0.02*(x**2).sum(1)
    utility = torque - loss
    y = np.stack([torque, loss, utility], axis=1)
    return x.astype(np.float32), y.astype(np.float32)

def train_surrogate(model, x, y, epochs=60):
    opt = optim.Adam(model.parameters(), lr=1e-3)
    loss_fn = nn.MSELoss()
    x_t, y_t = torch.tensor(x), torch.tensor(y)
    for e in range(1, epochs+1):
        opt.zero_grad()
        pred = model(x_t)
        loss = loss_fn(pred, y_t)
        loss.backward(); opt.step()
        if e % 10 == 0: print(f"[train] epoch {e}/{epochs} loss={loss.item():.6f}")
    return model

def evaluate(model, x, y_true):
    with torch.no_grad():
        y_pred = model(torch.tensor(x)).numpy()
    mse = ((y_pred - y_true)**2).mean(0)
    mae = np.abs(y_pred - y_true).mean(0)
    corr = [np.corrcoef(y_true[:,i], y_pred[:,i])[0,1] for i in range(3)]
    return dict(torque=corr[0], loss=corr[1], utility=corr[2]), mse, mae

def save_results(base, model, corr, mse, mae):
    os.makedirs(base, exist_ok=True)
    torch.save(model.state_dict(), f"{base}/de4_3x3_surrogate.pt")
    summary = {"corr":corr, "mse":mse.tolist(), "mae":mae.tolist()}
    json.dump(summary, open(f"{base}/summary.json","w"), indent=2)
    print("Saved results to:", base)

if __name__ == "__main__":
    base = "/content/motor_3x3_coupled_synthetic/results"
    x, y = gen_synthetic_data()
    model = DE4Surrogate3x3()
    model = train_surrogate(model, x, y)
    corr, mse, mae = evaluate(model, x, y)
    print("=== Summary ==="); print(corr)
    save_results(base, model, corr, mse, mae)
