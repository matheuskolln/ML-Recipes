from sklearn import tree # Importamos o Classificador que usaremos

features = [[140, 1], [130, 1], [150, 0], [170, 0]] # Características dos nossos dados
labels = [0, 0, 1, 1] # Classificação dos dados

classifier = tree.DecisionTreeClassifier() # Criando o classificador
classifier = classifier.fit(features, labels) # Treinando o classificador com nossos dados

print(classifier.predict([[150, 0]])) # Prevendo uma fruta de 150g com textura irregular, espera-se que seja uma laranja(1).