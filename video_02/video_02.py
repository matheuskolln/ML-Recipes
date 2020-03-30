# Importing dependencies | Importando dependências 
# Obs: This script depends on Graphviz, you need to run pip install graphviz | Este script depende do Graphviz, você precisa executar o pip install graphviz
import numpy as np 
from sklearn.datasets import load_iris
from sklearn import tree

# Loading dataset | Carregando conjunto de dados
iris = load_iris()

# Getting ID from one type of each species | Obtendo ID de um tipo de cada espécie
test_id_test = [0, 50, 100]

# Removing test data from training data | Removendo os dados de teste dos dados de treino
train_target = np.delete(iris.target, test_id_test)
train_data = np.delete(iris.data, test_id_test, axis=0)

# Getting the test data from dataset | Obtendo os dados de teste do conjunto de dados
test_target = iris.target[test_id_test]
test_data = iris.data[test_id_test]

# Classifying training data | Classificando os dados de treino
classifier = tree.DecisionTreeClassifier()
classifier.fit(train_data, train_target)

# Showing the real rating and the predicted rating | Mostrando a classificação real e a previsão.
print(f'Test target: {test_target}')
print(f'Predict target: {classifier.predict(test_data)}')

# Visualization Code of Decision Tree | Código de visualização da Árvore de Decisão
from sklearn.externals.six import StringIO
import pydot

dot_data = StringIO()

tree.export_graphviz(classifier,
                     out_file=dot_data,
                     feature_names=iris.feature_names,
                     class_names=iris.target_names,
                     filled=True, rounded=True,
                     impurity=False)

# I used this module (graphviz) to generate the graph
import graphviz as gp
graph = gp.Source(dot_data.getvalue())
graph.render("iris", view = True)