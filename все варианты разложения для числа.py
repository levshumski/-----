import numpy as np
import plotly.express as px
import pandas as pd
x=int(input('Введите число для проверки на фигурность: '))
sp=[]
msp=[]
for m in range(1,x//3+3):
    res=8*x*(m-2)+(m-4)*(m-4)
    if (np.sqrt(abs(res))).is_integer():
        sqres=np.sqrt(res)
        if sqres.is_integer():
            if m*2-4!=0:
                if ((sqres-4+m)/(2*m-4)).is_integer():
                    sp.append(int((sqres-4+m)/(2*m-4)))
                    msp.append(m)
for i in range(len(msp)):
    print('число '+str(x)+' является '+str(sp[i])+'-м по счету '+str(msp[i])+'-угольным числом')