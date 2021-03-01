import pandas as pd
from glob import glob

# Script instructions
print('\n\nAqui será feito a extracao do relatório semanal.')
print('Por favor, digite a data conforme a o modelo a seguir de ano, mês e dia:--> 20210108')
print('E a semana conforme o exemplo a seguir:--> Semana 2\n')

date_min = input('Digite a data que inicia a semana: ')
date_max = input('Digite a data que encerra a semana: ')
week_number = input('Qual seria a semana: ')

# Catching all files in the path. After that, all sort all the files in a list
files_assinantes = sorted(glob(r'base_assinantes/*.csv'))
files_logados_free = sorted(glob(r'base_lf/*.csv'))

# Reading all the files and concating them in a dataframe
df_a = pd.concat(pd.read_csv(file) for file in files_assinantes)
df_lf = pd.concat(pd.read_csv(file) for file in files_logados_free)

df_a['tipo_de_consumo'] = ['Aberto' if tipo_conteudo.lower() == 'aberto' else 'Fechado' for tipo_conteudo in df_a['Video - Fechado/Aberto']]

df_lf['tipo_de_consumo'] = 'Logado Free'

# Creating the main dataframe
df = pd.concat([df_a, df_lf])
df['semana'] = week_number

df['horas_consumidas'] = df['Video Playtime'] / 3600


df_group = df.groupby(['Video - ID do programa', 'tipo_de_consumo',]).\
			agg({'horas_consumidas': 'sum', 'Video Start': 'sum'})
