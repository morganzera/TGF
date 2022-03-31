import netCDF4 as nc
import pandas as pd

for i in range (2):
    ID_path = pd.read_excel('inventory_ID_path.xlsx')
    ds = nc.Dataset(ID_path['Inventory ID'][i])

    event_lat = ds['event_lat'][:]
    event_lon = ds['event_lon'][:]
    print(str(len(event_lat)) + " " + str(len(event_lon)))
### Par Latitude, longitude ###
    i = 0
    for i in range (len(event_lat)):
        coordenadas = event_lat[i], event_lon[i]
    # print(coordenadas)
        if (round(event_lat[i]) == 10.0 and round(event_lon[i]) == 6):
            print(event_lat[i], "### i = ", i)
            i = i + 1

# # print("Teste longitude:")
# # i = 0
# # for i in range (17303):
# #     coordenadas = event_lat[i], event_lon[i]
# #     # print(coordenadas)
# #     if (round(event_lon[i]) == 6.0):
# #         print(event_lon[i], "### i = ", i)
# #     i = i + 1