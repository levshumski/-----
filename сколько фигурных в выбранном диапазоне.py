import numpy as np
sp=[]
p=int(input())
k=int(input())
for x in range(p,k):
    for m in range(1,x//3+3):                       
        res=8*x*(m-2)+(m-4)*(m-4)
        if (np.sqrt(res)*10)%10==0:
            sqres=np.sqrt(res)
            if (sqres*10)%10==0:
                if ((sqres-4+m)/(2*m-4)*10)%10==0:
                    sp.append(x)
res=list(set(sp))
print(res)
print(len(res))
