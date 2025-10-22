#!/usr/bin/env python3
import os, numpy as np, pandas as pd
OUT_DIR="sample_output"; os.makedirs(OUT_DIR,exist_ok=True); np.random.seed(7)
def model(l,r,s):
 a=(0.8+0.2*l)*(1+0.12*(s-1)); t=a*(0.01*r)/(1+0.0005*r); h=0.0001*r**2*(1-0.3*l); g=0.5+0.45*l; m=t*r*0.01; e_out=max(0,m*g-h); eff=e_out/(a*r*0.02+1e-6); return m,e_out,eff
L=np.linspace(0.2,1.5,12); R=np.arange(500,4500,500); S=[1,2,3]; rows=[]
for l in L:
 for r in R:
  for s in S:
   m,e,f=model(l,r,s); rows.append(dict(lambda_L=l,rpm=r,stages=s,mech_power=m,elec_output=e,efficiency=f))
df=pd.DataFrame(rows); csv=f"{OUT_DIR}/ff_turbine_summary.csv"; df.to_csv(csv,index=False)
print("FF Turbine top 10:"); print(df.sort_values("efficiency",ascending=False).head(10)[["lambda_L","rpm","stages","efficiency","elec_output"]]); print("Saved:",csv)
