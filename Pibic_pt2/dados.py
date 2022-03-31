import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

datas = pd.read_excel('Fermi_Atualizado.xlsx')
for x in range(len(datas.loc[:, ('trigger_time')])):
    datas.loc[:, ('trigger_time')][x] = str(datas.loc[:, ('trigger_time')][x])[:10]

datas.loc[:, ('trigger_time')] = datas.loc[:, ('trigger_time')].astype("datetime64")
datas.loc[:, ('trigger_time')].groupby([datas.loc[:, ('trigger_time')].dt.year, 
                                        datas.loc[:, ('trigger_time')].dt.month]).count().plot(kind="bar")