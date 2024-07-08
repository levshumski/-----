import numpy as np
import plotly.express as px
sp=[]
dd=[]
mm=[]
for x in range(3,100001):
    for m in range(1,x//3+3):                       
        res=8*x*(m-2)+(m-4)*(m-4)
        sqres=np.sqrt(abs(res))
        if sqres.is_integer():
            if 2*m-4!=0:
                if ((sqres-4+m)/(2*m-4)).is_integer():
                    sp.append(x)
    if x%500==0:
        sp=list(set(sp))
        dd.append(len(sp))
        sp=[]
        mm.append(x)
fig=px.line(x=mm, y=dd, labels={'x':'Диапазон(D)', 'y':'Кол-во фигурных от D до D+500'})
fig.show()
