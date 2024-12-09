import math as mt
import plotly.express as px
import pandas as pd
import numpy as np

class vec:
    def __init__(self, m, a):   
        self.m = m  # Magnitude
        self.a = a  # Angle (in degrees)

def sumv(a, b):
    if b.a > a.a:
        a, b = b, a
    g = (a.a - b.a)
    x = a.m * mt.cos(mt.radians(g)) + b.m
    y = a.m * mt.sin(mt.radians(g))
    m = mt.sqrt(x * x + y * y)
    f = mt.degrees(mt.acos(x / m)) + b.a
    return vec(m, f)

def multv(a, k):
    return vec(a.m * k, a.a)

sp = []
msp = []
res1 = []
res2 = []

x = int(input("Введите число: "))

# Обновленные формулы для центрированных чисел
def centered_figurate(n, m):
    return (n*(n-1)*m+2)/2
# Определение возможных m (углы) и проверка на целые решения
for m in range(x//3+3):  # Для треугольных, квадратных и пятиугольных
    for n in range(1, x):
        if centered_figurate(n, m) == x:
            sp.append(n)
            msp.append(m)

print("m-угольные числа:", msp)
print("n для каждого числа:", sp)

def addv(vector):
    res1.append(vector.m)
    res2.append(vector.a)

# Генерация векторов и визуализация для центрированных чисел
for p in range(len(msp)):
    res1 = []
    res2 = []
    for i in range(sp[p]):
        v = vec(0, 0)  # Центр
        addv(v)
        
        for j in range(1, msp[p] + 1):
            z = (360 / msp[p]) * j  # Углы вокруг центра
            v1 = vec(i + 1, z)
            addv(v1)
    
    d = {'r': res1, 'theta': res2}
    df = pd.DataFrame(data=d)
    
    try:
        fig = px.line_polar(df, r='r', theta='theta',
                            markers=True, 
                            range_theta=[0, 360.0], range_r=[0.0, max(res1) + 0.5], 
                            start_angle=0, line_shape='linear', direction="counterclockwise",
                            title=f'Число {x} является центрированным {msp[p]}-угольным числом ({sp[p]} точек)')
    except:
        fig = px.scatter_polar(df, r='r', theta='theta',
                               range_theta=[0, 360.0], range_r=[0.0, max(res1) + 0.5], 
                               start_angle=0, direction="counterclockwise",
                               title=f'Число {x} является центрированным {msp[p]}-угольным числом ({sp[p]} точек)')
    
    fig.update_traces(line=dict(color="Red", width=0.5), marker=dict(color="Blue", size=3.5))
    fig.show()