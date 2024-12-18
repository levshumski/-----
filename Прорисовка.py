import math as mt
import plotly.express as px
import pandas as pd
import numpy as np

class vec:
    def __init__(self, m, a):   
        self.m = m;
        self.a = a;

def sumv(a, b):
    if (b.a > a.a):
        d = a
        a = b
        b = d
    g = (a.a - b.a)
    x = a.m * mt.cos(mt.radians(g)) + b.m
    y = a.m * mt.sin(mt.radians(g))
    m = mt.sqrt(x * x + y * y)
    f = mt.degrees(mt.acos(x / m)) + b.a
    return vec(m, f)

def multv(a, k):
    return vec(a.m * k, a.a)
sp=[]
msp=[]
res1 = []
res2 = []
x=int(input())
for m in range(1,x//3+3):
    res=8*x*(m-2)+(m-4)*(m-4)
    if (np.sqrt(res)).is_integer():
        sqres=np.sqrt(res)
        if (sqres*10)%10==0:
            if 2*m-4!=0:
                if ((sqres-4+m)/(2*m-4)).is_integer():
                    sp.append(int((sqres-4+m)/(2*m-4)))
                    msp.append(m)
print(msp)
print(sp)
def addv(vector):
    res1.append(vector.m)
    res2.append(vector.a)
for p in range(len(msp)):
    res1=[]
    res2=[]
    for i in range(sp[p]):
        v = vec(i, - 180 * (msp[p] - 2) / msp[p] / 2)
        for j in range(1, msp[p]):
            z = - 180 * (msp[p] - 2) / msp[p] / 2 + (360/msp[p])*j
            v1 = vec(1, z)                         
            addv(v)
            for _ in range(i):
                v = sumv(v, v1)
                addv(v)
    
    d = {'r': res1, 'theta': res2}
    df=pd.DataFrame(data=d)
    try:
        fig=px.line_polar(df, 'r', 'theta',
                            markers=True, 
                            range_theta=[0,360.0], range_r=[0.0,max(res1)+0.5], 
                            start_angle=0, line_shape='linear',direction="counterclockwise",title='Число '+str(x)+' является '+str(sp[p])+'-м '+str(msp[p])+' - угольным числом')
    except:
        fig=px.scatter_polar(df, 'r', 'theta',
                        range_theta=[0,360.0], range_r=[0.0,max(res1)+0.5], 
                        start_angle=0,direction="counterclockwise",title='Число '+str(x)+' является '+str(sp[p])+'-м '+str(msp[p])+' - угольным числом')

    fig.update_traces(line=dict(color="Red", width=0.5), marker=dict(color="Blue", size=3.5))
    fig.show()
