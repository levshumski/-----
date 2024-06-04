import math as mt
import plotly.express as px
import pandas as pd

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

m = 3
n = 55

res1 = []
res2 = []

def addv(vector):
    res1.append(vector.m)
    res2.append(vector.a)

for i in range(n):
    v = vec(i, - 180 * (m - 2) / m / 2)
    for j in range(1, m - 1):
        z = - 180 * (m - 2) / m / 2 + (360/m)*j
        v1 = vec(1, z)
        addv(v)
        for _ in range(i):
            v = sumv(v, v1)
            addv(v)

d = {'r': res1, 'theta': res2}
df = pd.DataFrame(data=d)
fig = px.scatter_polar(df, 'r', 'theta', range_theta=[0,360.0], range_r=[0.0,max(res1)], start_angle=0, direction="counterclockwise")
fig.show()