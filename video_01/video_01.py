from sklearn import tree # Importamos o Classificador que usaremos | We import the Classifier that we will use

features = [[140, 1], [130, 1], [150, 0], [170, 0]] # Características dos nossos dados | Features of our data
labels = [0, 0, 1, 1] # Classificação dos dados | Labels of data

classifier = tree.DecisionTreeClassifier() # Criando o classificador | Creating the classifier
classifier = classifier.fit(features, labels) # Treinando o classificador com nossos dados | Training the classifier with our data

print(classifier.predict([[150, 0]])) # Prevendo uma fruta de 150g com textura irregular, espera-se que seja uma laranja(1).
                                      # Predicting a 150g fruit with a bumpy texture, it is expected to be an orange (1).