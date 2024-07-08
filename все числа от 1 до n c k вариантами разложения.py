import numpy as np
import math
n=int(input())
sp=[]
b=3
for m in range(3,n//3+3):
    b=3
    while (b*(b-1)*(m-2)+2*b)/2<n:
        sp.append((b*(b-1)*(m-2)+2*b)/2)
        b+=1
sp=list(set(sp))
new=[]
for i in sp:
    func=[]
    for m in range(3,int(i)//3+3):
        res=8*i*(m-2)+(m-4)*(m-4)
        if (np.sqrt(res)*10)%10==0:
            sqres=np.sqrt(res)
            if (sqres*10)%10==0:
                if ((sqres-4+m)/(2*m-4)*10)%10==0:
                    func.append(m)
    if len(func)>=1:
        new.append(i)
print(new)