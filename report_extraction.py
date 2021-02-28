import pandas as pd
from glob import glob

# Script instructions
print('\n\nAqui será feito a extracao do relatório semanal.')
print('Por favor, digite a data conforme a o modelo a seguir de ano, mês e dia: 20210108\n')

date_min = input('Digite a data que inicia a semana: ')
date_max = input('Digite a data que encerra a semana: ')

# Catching all files in the path. After that, all sort all the files in a list
files = sorted(glob(r'base/*.csv'))

# Reading all the files and concating them in a dataframe
df = pd.concat(pd.read_csv(file) for file in files)




