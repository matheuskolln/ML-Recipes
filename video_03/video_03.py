# Importing dependencies | Importando as dependências
import numpy as np 
import matplotlib.pyplot as plt

# Creating data | Criando dados
greyhounds = 500
labradors = 500

# Creating height for the data | Criando altura para os dados
greyhound_height = 71 + 10 * np.random.randn(greyhounds)
labrador_height = 61 + 10 * np.random.randn(labradors)

# Histogram | Histograma
plt.hist([greyhound_height, labrador_height], stacked=True, color=['r', 'b']) # Red for Greyhounds and Blue for Labradors | Vermelho para Galgos Ingleses e Azul para Labradores
plt.show()