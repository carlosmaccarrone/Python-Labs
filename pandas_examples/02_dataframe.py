array_2d = [ [3.3, 4.4], [5.5, 6.6], [7.7, 8.8] ]

print( array_2d )
print( array_2d[0][1] )
print('\n')

import pandas as pd
df = pd.DataFrame(array_2d)

print( df )
print( df[1][0]) 
print( df.columns )
print('\n')

df.columns = ["Primero", "Segundo"]

print( df )
print( df["Segundo"] ) # Since it is a column, it is no longer a data frame but a series.




