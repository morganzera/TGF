import pandas as pd
import netCDF4 as nc


# Refatorando a tabela coordenadasTGF:
coordenadasTGF = pd.read_excel('coordenadasTGF.xlsx')
tabelaGeral = pd.read_excel('tabelaGeral.xlsx')
ref = []
# for x in range(1):
for x in range(len(tabelaGeral)):
    for i in range(len(coordenadasTGF)):
        trigger = str(coordenadasTGF['trigger_time'][i])
        trigger = trigger[:10] + "," + trigger[11:]
        trigger = trigger.split(",")

        data_trigger = trigger[0]
        hora_trigger = trigger[1][:8]

        hora_fermi = str(tabelaGeral['hora FERMI'][x])
        data_fermi = str(tabelaGeral['data FERMI'][x])

        if data_trigger == data_fermi and hora_fermi[:2] == hora_trigger[:2]:
            ref.append([tabelaGeral['data noaa'][x], 
                tabelaGeral['hora noaa'][x], 
                tabelaGeral['data FERMI'][x], 
                tabelaGeral['hora FERMI'][x],
                coordenadasTGF['geo_lon'][i],
                coordenadasTGF['geo_lat'][i], 
                tabelaGeral['id'][x], 
                tabelaGeral['ID path'][x]])
            

tabelaGeral_v2 = pd.DataFrame(ref, columns=['data noaa','hora noaa', 'data FERMI', 'hora FERMI', 'geo_lon', 'geo_lat', 'id', 'ID path'])
print(tabelaGeral_v2)
# tabelaGeral_v2.to_excel('tabelaGeral_v2.xlsx',index=False)

# dadoNOAA = nc.Dataset(r'C:\Users\PC\Documents\Pibic_py\Pibic\Dados\OR_GLM-L2-LCFA_G16_s20192920447400_e20192920448000_c20192920448022.nc')
# dataNOAA = str(dadoNOAA)
# print(dataNOAA)

# arquivo = pd.read_excel(r'C:\Users\PC\Documents\Pibic_py\inventory_ID.xlsx')
# print(len(arquivo))
# data_fermi = pd.read_excel(r'C:\Users\PC\Documents\Pibic_py\Pibic\Data_fermi.xlsx')
# print(data_fermi)

"""
Tenho 167 dados/datas NOAA
Tenho 162 dados TGF FERMI
"""