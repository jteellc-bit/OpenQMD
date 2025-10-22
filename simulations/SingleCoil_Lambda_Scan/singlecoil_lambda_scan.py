#!/usr/bin/env python3
import os, numpy as np, pandas as pd
OUT_DIR="sample_output"; os.makedirs(OUT_DIR,exist_ok=True); np.random.seed(42)
def oracle(s,l):a,r,b=s; t=(np.sin(a)*(0.5+0.5*l))+0.1*r+0.02*b; L=0.2*np.cos(r+0.3*a)*(1-0.4*l)+0.01*b; e=(t-0.4*abs(L))/(1+abs(t)+abs(L)); return t,L,e
vals=np.linspace(0.1,1.5,25); rows=[]
for l in vals:
 tL,lL,eL=[],[],[]
 for _ in range(256):s=np.random.uniform(-1,1,3);t,L,e=oracle(s,l);tL.append(t);lL.append(L);eL.append(e)
 tL,lL,eL=np.array(tL),np.array(lL),np.array(eL)
 rows.append(dict(lambda_L=l,mean_efficiency=np.mean(eL),std_efficiency=np.std(eL),torque_rms=np.sqrt(np.mean(tL**2)),mean_torque=np.mean(tL),mean_loss=np.mean(lL),n_samples=256))
df=pd.DataFrame(rows); csv=f"{OUT_DIR}/singlecoil_summary_table.csv"; df.to_csv(csv,index=False)
print("SingleCoil λ_L sweep top 10:"); print(df.sort_values("mean_efficiency",ascending=False).head(10)[["lambda_L","mean_efficiency","std_efficiency","torque_rms"]]); print("Saved:",csv)
