import pandas as pd

pd.set_option('display.max_columns', 10) # by default it is at 2

dataframe = pd.read_csv('artist_data.csv') 

print( dataframe )
print( dataframe.columns )
print('\n')

dataframe['url'] = "hello world"

print( dataframe )
print( dataframe.columns )
print('\n')

del dataframe['url']

print( dataframe )
print( dataframe.columns )
print('\n')

##dataframe.loc[dataframe["gender"] == "Male", "dates"] = 888

dataframe.to_json('json_file.json')
dataframe.to_excel('artist_data.xlsx', sheet_name='Página Uno', index=False)
dictionaries_list = dataframe.to_dict(orient='records')

print(dictionaries_list[:1])



