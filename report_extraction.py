import pandas as pd
from glob import glob

# Script instructions
print('\n\nAqui será feito a extracao do relatório semanal.')
print('Por favor, digite a data conforme a o modelo a seguir de ano, mês e dia:--> 20210108')
print('E a semana conforme o exemplo a seguir:--> Semana 2\n')

date_min = int(input('Digite a data que inicia a semana: '))
date_max = int(input('Digite a data que encerra a semana: '))
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
# Filtering the data
week_filter = (df['Data'] >= date_min) & (df['Data'] <= date_max)
df = df.loc[week_filter]

df['horas_consumidas'] = df['Video Playtime'] / 3600

# Creating the column to classify the type of consumption
df['Tipo de Consumo'] = \
['Live' if tipo_video.lower() == 'live' else\
'VOD Aberto' if tipo_consumo == 'Aberto' else\
'VOD Fechado' if tipo_consumo == 'Fechado' else\
'VOD Logado Free' if tipo_consumo == 'Logado Free' else\
'null'\
for tipo_video, tipo_consumo in zip(df['Video - Tipo de video'], df['tipo_de_consumo'])]


df_final = pd.DataFrame(df.groupby(['Video - ID do programa', 'Tipo de Consumo', 'Semana'])['horas_consumidas', 'Video Start'].sum()).reset_index()

