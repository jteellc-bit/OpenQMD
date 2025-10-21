import numpy as np

def run_simple_mpc(eval_fn, steps=30, n_cand=60, rng=None):
    rng = np.random.default_rng() if rng is None else rng
    theta = rng.uniform(0, 2*np.pi)
    logs = {'theta':[], 'torque':[], 'loss':[], 'utility':[], 'I':[], 'p':[]}
    for _ in range(steps):
        I = np.clip(rng.normal(1.0, 0.6, n_cand), 0.0, 2.5)
        p = rng.choice([-1.0,0.0,1.0], n_cand, p=[0.45,0.1,0.45])
        cand = np.vstack([np.full(n_cand, theta), I, p]).T
        results = [eval_fn(c) for c in cand]
        utilities = [r[2] for r in results]
        idx = int(np.argmax(utilities))
        best = results[idx]
        logs['theta'].append(theta)
        logs['torque'].append(best[0])
        logs['loss'].append(best[1])
        logs['utility'].append(best[2])
        logs['I'].append(I[idx])
        logs['p'].append(p[idx])
        theta = (theta + 0.12 * best[0]) % (2*np.pi)
    return logs
