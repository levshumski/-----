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
data1=[]
data2=[]
'''for i in range(x):
    data1.append(180*(m-2)/m)
    if msp[0]
    data2.append(i)'''
# d = {'r': [2,3], 'theta': [0,1]}
# df = pd.DataFrame(data=d)
# fig = px.scatter_polar(df, 'r', 'theta', range_theta=[0,360.0], range_r=[0.0,4.0], start_angle=0, direction="counterclockwise")
# fig.show()