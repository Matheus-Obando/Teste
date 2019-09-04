#importa as bibliotecas necessárias:
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Armazena os dados de ambas as abas em um dataframe:
excel_file = 'dados.xlsx'
orcado = pd.read_excel(excel_file, sheet_name='orcado')
realizado = pd.read_excel(excel_file, sheet_name='realizado')

print(orcado)
realizado = realizado.T # Transpõe os valores do dataframe
realizado = realizado.drop(realizado.index[0]) # remove a primeira linha do dataframe transposto
realizado.columns = ['mês', 'realizado'] # renomeia as colunas do dataframe
print(realizado)

merged = orcado.merge(realizado, how = 'right', on = 'mês') # faz o merge entre os dataframes
print(merged)
merged['diff'] = merged['orcado'] - merged['realizado'] # cria uma nova coluna a qual subtrai os valores das duas colunas
print(merged)

merged.to_csv('saida.csv') # Envia o dataframe para um arquivo de saída

# Plot gráfico (gráfico de barras):
n_barras = 12 # numero de barras do gráfico (todos os meses)
orc_lista = merged['orcado'].tolist()
rea_lista = merged['realizado'].tolist()
meses_lista = merged['mês'].tolist()
ind = np.arange(n_barras) # cria um array de 0 a n_barras-1

# constroi o gŕafico
plt.bar(ind, orc_lista, width=0.8)
plt.bar(ind, rea_lista, width=0.8)

plt.title('Gráfico Orçamento')
plt.xticks(ind, meses_lista)
plt.yticks(np.arange(0, 500, 100))
plt.ylabel('$')
plt.xlabel('Mês')
plt.legend(('Orçado', 'Realizado'), loc='upper left')

# Exibe o gráfico
plt.show()