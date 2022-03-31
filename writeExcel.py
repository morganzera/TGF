import pandas as pd
import os
pasta = r'C:\Users\pc\Documents\Pibic_py\Pibic\Dados'
ref = []
for diretorio, subpasta, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        arquivo = str(arquivo)
        arquivo = str(r'C:\Users\pc\Documents\Pibic_py\Pibic\Dados\ ') + arquivo[:]
        arquivo = arquivo.replace(" ", "")
        # arquivo = "r\'" + arquivo[:] + "\'"
        ref.insert(len(ref), [arquivo])

lst_dados = pd.DataFrame(ref, columns=['Inventory ID'])
# lst_dados.to_excel('inventory_ID.xlsx', index=False)
print(lst_dados)