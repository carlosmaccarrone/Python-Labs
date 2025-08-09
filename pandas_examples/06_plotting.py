import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv('artist_data.csv')
dataframe = dataframe[:20]
dataframe = dataframe[ (dataframe['yearOfBirth'] >= 1850) & (dataframe['yearOfDeath'] < 1975) ]

# ####
fig, ax = plt.subplots()
ax.scatter(x=dataframe['yearOfBirth'], y=dataframe['yearOfDeath'], c='DarkBlue')
ax.set_xlabel('Año nacimiento')
ax.set_ylabel('Año defunción')
for _, row in dataframe.iterrows():
    ax.annotate(row['name'], (row['yearOfBirth'], row['yearOfDeath']), 
        xytext=(10,-5), 
        textcoords='offset points',
        family='sans-serif', 
        fontsize=18, 
        color='darkslategrey' 
        )
plt.suptitle('Manipulacion y analisis de datos', fontsize=18) 
plt.show()
# ####

####
spainPopulation = [ (2006, 4.0), (2007, 5.2), (2008, 5.9),
                    (2009, 6.3), (2010, 6.5), (2011, 6.6),
                    (2012, 6.7), (2013, 6.5), (2014, 6.4),
                    (2015, 6.3) ]
spainPopulation = pd.DataFrame.from_records(spainPopulation, columns=['age', 'population'])
spainPopulation.plot(kind="bar", x='age', y='population')
plt.show() 
####

