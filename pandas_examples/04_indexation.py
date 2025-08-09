import pandas as pd

dataframe = pd.read_csv('artist_data.csv')
dataframe = dataframe[:20]
del dataframe['url']
copiaDeSeguridad = dataframe.copy()
pd.set_option('display.max_columns', 10) 
print(dataframe)

dataframe = dataframe[ dataframe['yearOfBirth'] >= 1890 ]
print(dataframe)

dataframe.reset_index(drop=True, inplace=True)
print( dataframe )

onlyRowByLoc = dataframe.loc[12] # busca la fila que corresponda a 
print( onlyRowByLoc )			 # al indice 12

dataframe.loc[dataframe["gender"] == "Male", "dates"] = "hello world"
print( dataframe )

newIndexDf = copiaDeSeguridad.set_index('name')
onlyRowByLoc = newIndexDf.loc['Agar, Eileen'] # consulta por el indice
print( onlyRowByLoc )

onlyRowByIloc = dataframe.iloc[12] # cuenta desde 0 (primer fila) 
print( onlyRowByIloc )			   # hasta 12

onlyRowByIloc = dataframe.iloc[ [12, 5, 8] ] 
print( onlyRowByIloc )			   

dataframe = dataframe[ (dataframe['yearOfBirth'] >= 1925) & (dataframe['gender'] == 'Female') ]
print(dataframe)
 
