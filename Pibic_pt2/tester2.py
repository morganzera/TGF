import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def ricker(f, length=0.512, dt=0.001):
    t = np.linspace(-length/2, (length-dt)/2, length/dt)
    y = (1.-2.*(np.pi**2)*(f**2)*(t**2))*np.exp(-(np.pi**2)*(f**2)*(t**2))
    return t, y

datas = pd.read_excel('Data_fermi.xlsx')
datas['D'] = datas['D'].astype("datetime64")
contagem = datas['D'].groupby([datas["D"].dt.year, datas["D"].dt.month]).count()

print(datas['D'].dt.year)