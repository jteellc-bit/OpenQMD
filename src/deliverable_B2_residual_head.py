# Residual_Head_Trainer
# Residual trainer demo (synthetic)
# This is a synthetic demo: it writes a summary CSV to results/ and prints the output path.
import os, numpy as np, pandas as pd
from datetime import datetime

OUTDIR = os.path.join(os.getcwd(), "results", "residual_head_trainer")
os.makedirs(OUTDIR, exist_ok=True)

def main():
    rng = np.random.RandomState(0)
    lambda_L = np.linspace(0.1, 1.5, 12)
    rows = []
    for lam in lambda_L:
        vals = rng.normal(loc=lam*0.2, scale=0.1, size=50)
        rows.append({"lambda_L": float(lam), "mean_eff": float(vals.mean()), "std_eff": float(vals.std())})
    df = pd.DataFrame(rows)
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    out_csv = os.path.join(OUTDIR, f"residual_head_trainer_summary_{ts}.csv")
    df.to_csv(out_csv, index=False)
    print("Saved summary to:", out_csv)

if __name__ == "__main__":
    main()
