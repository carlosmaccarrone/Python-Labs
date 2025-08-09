array_np = [ 3.3, 4.4, 5.5 ]

print( type(array_np) )
print( array_np[0] )
print( array_np )
print('\n')

import pandas as pd
series = pd.Series(array_np)

print( series[0] ) # The series looks like the array but it is indexed.
print( series )
print( series.index )
print('\n')

series = pd.Series(array_np, index=["Tercero", "Segundo", "Primero"])

print( series["Primero"] )
print( series[0] )
print( series )
print( series.index )



