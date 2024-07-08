import numpy as np
sp=[]
k=int(input())
m=3
for x in range(1,k):                     
    res=8*x*(m-2)+(m-4)*(m-4)
    if (np.sqrt(res)*10)%10==0:
        sqres=np.sqrt(res)
        if (sqres*10)%10==0:
            if ((sqres-4+m)/(2*m-4)*10)%10==0:
                sp.append(x)
print(len(sp))