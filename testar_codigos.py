import pandas as pd
# List of Tuples
fruit_list = [ ('Orange', 34, 'Yes' )]
#Create a DataFrame object
df = pd.DataFrame(fruit_list, columns = ['Name' , 'Price', 'Stock'])
#Add new ROW
df=df.append({'Name' : 'Apple' , 'Price' : 23, 'Stock' : 'No'} , ignore_index=True)
df=df.append({'Name' : 'Mango' , 'Price' : 13, 'Stock' : 'Yes'} , ignore_index=True)
print(df)

def adicionar0(original, mais):
    referencia = original.append(mais)