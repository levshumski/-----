import numpy as np
import plotly.express as px
import pandas as pd
import math
x=int(input())
sp=[]
msp=[]
for m in range(1,x//3+3):
    res=8*x*(m-2)+(m-4)*(m-4)
    if (np.sqrt(res)*10)%10==0:
        sqres=np.sqrt(res)
        if (sqres*10)%10==0:
            if ((sqres-4+m)/(2*m-4)*10)%10==0:
                sp.append(int((sqres-4+m)/(2*m-4)))
                msp.append(m)
print(msp)
print('-------------------------')
print(sp)