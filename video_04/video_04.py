# Import a dataset | Importando um conjunto de dados
from sklearn import datasets, tree

# Creating dataset | Criando o conjunto de dados
iris = datasets.load_iris()

# We can think about classifier like a function f(x) = y | Podemos pensar no classificador como uma função f (x) = y
X = iris.data # Features
y = iris.target # Labels

# Partitioning in Train and Test | Particionando em Treino e Teste
from sklearn.model_selection import train_test_split
# X_train and y_train are features and labels from training set, and X_test and y_test are features and labels from testing set
# X_train e y_train são features e labels do conjunto de treinamento e X_test e y_test são features e labels do conjunto de testes
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5) # 50% of data will be used to test | 50% dos dados serão usados para testar

from sklearn.neighbors import KNeighborsClassifier
# Creating classifier 1 | Criando classificador 1
my_classifier = tree.DecisionTreeClassifier()
# Creating classifier 2 | Criando classificador 2
my_classifier2 = KNeighborsClassifier()

# Training the classifier 1 | Treinando o classificador 1
my_classifier.fit(X_train, y_train)
# Training the classifier 2 | Treinando o classificador 2
my_classifier2.fit(X_train, y_train)

# Predictions 1| Previsões 1
predictions = my_classifier.predict(X_test)
# Predictions 2| Previsões 2
predictions2 = my_classifier2.predict(X_test)

# Accuracy | Precisão 
from sklearn.metrics import accuracy_score
print(f'Accuracy Score of Decision Tree: {accuracy_score(y_test, predictions)}')
print(f'Accuracy Score of KNeighborsClassifier: {accuracy_score(y_test, predictions2)}')