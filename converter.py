import pandas as pd
import netCDF4 as nc


# Refatorando a tabela coordenadasTGF:
coordenadasTGF = pd.read_excel('coordenadasTGF.xlsx')
ref =[]

for i in range (len(coordenadasTGF)):
    ref.append([coordenadasTGF['geo_lon'][i], coordenadasTGF['geo_lat'][i], coordenadasTGF['trigger_time'][161-i]])
    
coordenadasTGF = pd.DataFrame(ref,columns=['geo_lon', 'geo_lat', 'trigger_time'])
coordenadasTGF.to_excel('coordenadasTGFok.xlsx', index=False)
print(coordenadasTGF)