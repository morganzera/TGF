with open('Coordenadas.txt', 'w') as lst_coordenadas:
    import netCDF4 as nc

    diretorio = r'C:\Users\pc\Documents\Pibic_py\Pibic\Dados\OR_GLM-L2-LCFA_G16_s20212610131000_e20212610131200_c20212610131223.nc'
    ds = nc.Dataset(diretorio)

# print(ds)

    print("###############################################")

    event_lat = ds['event_lat'][:]
    event_lon = ds['event_lon'][:]
    print("Quantidade de latitudes: ", len(event_lat))
    print("Quantidade de longitudes: ", len(event_lon))
    print(ds)
### Par Latitude, longitude ###
    # i = 0
    # for i in range (17303):
    #     coordenadas = event_lat[i], event_lon[i]
    # # print(coordenadas)
    #     if (round(event_lat[i]) == 10.0 and round(event_lon[i]) == 6):
    #         print(event_lat[i], "### i = ", i, file = lst_coordenadas)
    #     i = i + 1
# print("Teste longitude:")
# i = 0
# for i in range (17303):
#     coordenadas = event_lat[i], event_lon[i]
#     # print(coordenadas)
#     if (round(event_lon[i]) == 6.0):
#         print(event_lon[i], "### i = ", i)
#     i = i + 1