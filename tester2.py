import netCDF4 as nc

arquivo = nc.Dataset(r'C:\Users\PC\Documents\Pibic_py\Pibic\Dados\OR_GLM-L2-LCFA_G16_s20192920447400_e20192920448000_c20192920448022.nc')
latNOAA = arquivo['event_lat'][:]
lonNOAA = arquivo['event_lon'][:]

print(latNOAA)
print(lonNOAA)