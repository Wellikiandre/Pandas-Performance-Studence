# -*- coding: utf-8 -*-
"""pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10LeLmnQg3aqhI_yxU0yH9A5hgqny_fBr
"""

#Importando da máquina local.

#from google.colab import files 
#uploaded = files.upload()
#import pandas as pd 
#import io 
  
#df = pd.read_csv(io.BytesIO(uploaded['nomeDoArquivo.csv'])) 
#df

#Importando do github
# É a maneira mais fácil de fazer upload de um arquivo CSV no Colab.
# Para isso vá para o conjunto de dados em seu repositório github e clique em “View Raw” . 
# Copie o link para o conjunto de dados bruto e passe-o como parâmetro para read_csv() no pandas para obter o dataframe. 

import pandas as pd 
url = 'https://raw.githubusercontent.com/Wellikiandre/Pandas-Performance-Studence/master/Analitico/StudentsPerformance.csv'
df = pd.read_csv(url)

type(df)

#5 Primeiras linhas
df.head()

#ultimas 5 linhas
df.tail()

#total de linhas e colunas
df.shape

#nome das colunas
df.columns

#verifica duplicatas
df.duplicated().sum()

# Verificar as informações das colunas , quantidade de not null e o tipo dos dados
df.info()

#Verifica a quantidade de null por colunas
df.isna().sum()

#Sumário estatístico
df.describe()

# Sumário estatístico inclusive para variáveis categóricas
df.describe(include='all')

#Quantidade de valores unicos por coluna
df.nunique()

# Ver os valores unicos dentro da coluna selecionada
df['gender'].unique()

# ver a distribuição entre valores unicos dentro da coluna
df.gender.value_counts()

#Vetor de ordenação
provas = ['math score', 'reading score', 'writing score']
#comando de ordenação (\) deixa continuar o argumento
df = df.sort_values(by = provas, ascending= False)\
.reset_index(drop = True)
df

df['median'] = df[provas].mean(axis=1)
df

#consultas
df[(df.gender == 'male') & (df['test preparation course'] == 'none') & (df['math score']>=70)]