"""
Objetivo: verificar se as coordenadas do relampago registrados pelo noaa é igual ou proximo das coordenadas do tgf registrados pelo Fermi.
"""
from operator import index
import netCDF4 as nc
import pandas as pd

def formatar(x):
    x = x.replace("T","")
    x = x[:10] + "," + x[10:]
    x = x.replace(".0Z","")
    x = x.split(",")
    return x

# Definir os caminhos das dbs.
tabela_fermi = pd.read_excel(r'C:\Users\PC\Documents\Pibic_py\Pibic\Data_fermi.xlsx')
inventory_id = pd.read_excel('inventory_ID.xlsx')
ID_path = pd.read_excel('inventory_ID_path.xlsx')
ref1 = []
ref2 = []

# Abrir os varios dados netcdf.
for i in range (len(ID_path)):
# for i in range (26):
    dadoNOAA = nc.Dataset(ID_path['Inventory ID'][i])
    #formatar o netcdf.
    dataNOAA = str(dadoNOAA.__dict__['time_coverage_start'])
    dataNOAA = formatar(dataNOAA)
    ref2.append(dataNOAA)
    tabela_dataNOAA = pd.DataFrame(ref2, columns=['data noaa', 'hora noaa'])
    dataNOAA = tabela_dataNOAA['data noaa'][i]
    horaNOAA = tabela_dataNOAA['hora noaa'][i]
# Abrir a db do fermi
    for x in range (len(tabela_fermi)):
    # Formatar a db.
        dataFERMI = str(tabela_fermi['D'][x])
        horaFERMI = str(tabela_fermi['H'][x])
        dataFERMI = dataFERMI.replace(" 00:00:00","")
    # Verificar para qual index/row na db do fermi corresponde esse netcdf.
        # Primeira filtragem: data
        # Segunda filtragem: hora
        if dataFERMI == dataNOAA and horaFERMI[:2] == horaNOAA[:2]:
            informacoes = [dataNOAA, horaNOAA, dataFERMI, horaFERMI, inventory_id['Inventory ID'][i], ID_path['Inventory ID'][i]]
            ref1.append(informacoes)

tabela_DataNOAAxID = pd.DataFrame(ref1, columns=['data noaa','hora noaa', 'data FERMI', 'hora FERMI', 'id', 'ID path'])
                # tabela_DataNOAAxID.to_excel('tabelaGeral.xlsx',index=False)

# Verificar se nesse netcdf há alguma coordenada que bate com o do fermi.
tabelaGeral_v2 = pd.read_excel('tabelaGeral_v2.xlsx')
tabelaGeral_v2['geo_lat'] = pd.to_numeric(tabelaGeral_v2['geo_lat'], errors="coerce")
tabelaGeral_v2['geo_lon'] = pd.to_numeric(tabelaGeral_v2['geo_lon'], errors="coerce")
a = 0
coordenadas_matched_completed = []
for x in range (1):
# for x in range (len(tabelaGeral_v2['ID path'])):
    coordenadas_matched = []
    coordenadas = []
    dadoNOAA = nc.Dataset(tabelaGeral_v2['ID path'][x])
    qtdeCoord = dadoNOAA['event_lat'][:]
    for i in range (len(qtdeCoord)):
        latNOAA = str(dadoNOAA['event_lat'][i:i+1])
        latNOAA = latNOAA.replace("[", "").replace("]", "")
        lonNOAA = str(dadoNOAA['event_lon'][i:i+1])
        lonNOAA = lonNOAA.replace("[", "").replace("]", "")
        
        coordenadas.append([latNOAA, lonNOAA])    # coordenadas = [[latNOAA1, lonNOAA1], [latNOAA2, lonNOAA2]...]

        indiceLat = str(coordenadas[i][0]).find('.')
        lat_do_NOAA = str(coordenadas[i][0])[:(indiceLat+3)]
        lat_do_NOAA = float(lat_do_NOAA)
        latN = lat_do_NOAA
        lat_do_NOAA = round(lat_do_NOAA, 0)

        indiceLon = str(coordenadas[i][1]).find('.')
        lon_do_NOAA = str(coordenadas[i][1])[:(indiceLon+3)]
        lon_do_NOAA = float(lon_do_NOAA)
        lonN = lon_do_NOAA
        lon_do_NOAA = round(lon_do_NOAA, 0)

        latTGF = tabelaGeral_v2['geo_lat'][x]
        latT = latTGF
        latTGF = round(latTGF,0)

        lonTGF = tabelaGeral_v2['geo_lon'][x]
        lonT = lonTGF
        lonTGF = round(lonTGF,0)
        # print("lat_do_NOAA: ", lat_do_NOAA, "latTGF: ", latTGF, lat_do_NOAA == latTGF)
        # print("lon_do_NOAA: ", lon_do_NOAA, "##", "lonTGF: ", lonTGF, lon_do_NOAA == lonTGF)
        # print("_______________________________________")
        if lat_do_NOAA == latTGF and lon_do_NOAA == lonTGF:
            coordenadas_matched.append([latT, lonT, tabelaGeral_v2['id'][x]])
            contagem = coordenadas_matched.count([latT, lonT, tabelaGeral_v2['id'][x]])
            if contagem > 1:
                coordenadas_matched.pop(len(coordenadas_matched)-1)
    if len(coordenadas_matched) != 0:
        a += 1
        print(coordenadas_matched, "x = ", x, "/", len(tabelaGeral_v2['ID path']), "Quantidade de match: ", a, "/", len(tabelaGeral_v2['ID path']))
    else:
        print("Nenhuma coordenada batendo. x = ", x, "/", len(tabelaGeral_v2['ID path']))
    if len(coordenadas_matched) != 0:
        coordenadas_matched_completed.append(coordenadas_matched)
    print(coordenadas_matched_completed)
# Retornar um excel com o id do netcdf e o index/row do fermi para os que baterem a coordenada.
matches = pd.DataFrame(coordenadas_matched_completed, columns=['Lista de matches'])
matches.to_excel('matches.xlsx', index=False)