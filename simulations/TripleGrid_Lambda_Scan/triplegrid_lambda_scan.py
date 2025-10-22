#!/usr/bin/env python3
import os, numpy as np, pandas as pd
OUT_DIR="sample_output"; os.makedirs(OUT_DIR,exist_ok=True); np.random.seed(123)
def oracle(s,l):
 psi=[np.array([np.cos(2*np.pi*x),np.sin(2*np.pi*x),0.2*x])*(0.6+0.4*l) for x in s]
 psi=np.stack(psi); psi/=np.linalg.norm(psi,axis=1,keepdims=True)+1e-9
 c=(np.sum(np.abs(np.dot(psi,psi.T)))-9)/(9*8); t=float(np.sum(psi[:,0])*(0.2+0.8*c)); L=float((1-c)*(0.5-0.2*l)); e=(t-0.5*L)/(1+abs(t)+abs(L)); return t,L,e,c
vals=np.linspace(0.1,1.5,20); rows=[]
for l in vals:
 E,T,L,C=[],[],[],[]
 for _ in range(200):s=np.random.uniform(-1,1,9);t,x,e,c=oracle(s,l);E.append(e);T.append(t);L.append(x);C.append(c)
 rows.append(dict(lambda_L=l,mean_eff=np.mean(E),std_eff=np.std(E),mean_torque=np.mean(T),std_torque=np.std(T),mean_loss=np.mean(L),mean_coherence=np.mean(C),n_trials=200))
df=pd.DataFrame(rows); csv=f"{OUT_DIR}/triplegrid_summary.csv"; df.to_csv(csv,index=False)
print("TripleGrid λ_L sweep top 8:"); print(df.sort_values("mean_eff",ascending=False).head(8)[["lambda_L","mean_eff","std_eff","mean_coherence"]]); print("Saved:",csv)
