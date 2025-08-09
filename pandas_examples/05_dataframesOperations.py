import pandas as pd

data = [(3,5,7), (2,4,6), (5,8,9)]
dataframe = pd.DataFrame(data, columns=['A', 'B', 'C'])
print( dataframe )
print('\n')

dataframe2 = dataframe.apply(lambda x: x+10)
print( dataframe2 )
print('\n')

dataframe2['A'] = dataframe2['A'].map(lambda y: y/2)
print( dataframe2 )
print('\n')

data2 = [(1,0,0), (0,1,0), (0,0,1)]
dataframe3 = pd.DataFrame(data2, columns=['A', 'B', 'C'])
print( dataframe3 )
print('\n')

# dataframe4 = dataframe2.append(dataframe3) # deprecated
dataframe4 = pd.concat([dataframe2, dataframe3], ignore_index=True)
print( dataframe4 )






