from scipy.spatial import distance # (Step 6)

def euc(a, b):
    return distance.euclidean(a, b)

# Creating the class of our classifier | Criando a classe do nosso classificador 
class ScrappyKNN():
    def fit(self, X_train, y_train): # (Step 3)
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test, y_test): # (Step 3)
        predictions = []
        for row in X_test:
            label = self.closest(row) # Close Point | Ponto Próximo
            predictions.append(label)
        return predictions

    def closest(self, row): # (Step 7)
        best_dist = euc(row, self.X_train[0]) # We define a standard point as closest | Definimos um ponto padrão como mais próximo
        best_index = 0 # We define a standard index for this point | Definimos um index padrão para este ponto
        for i in range(1, len(self.X_train)): # Iterate all points | Iteramos todos os pontos 
            dist = euc(row, self.X_train[i]) # Calculate the Euclidean Distance | Calculamos a Distância Euclidiana
            if dist < best_dist: # If the calculated distance is less than the current one, it takes it as the smallest and changes the index 
                best_dist = dist # Se a distância calculada for menor que a atual, ele toma-a como a menor e muda o index 
                best_index = i
        return self.y_train[best_index] # Returns the label with best index, because this is from the smallest distance
                                        # Retorna o label com o melhor index, porque este é o da menor distância


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

# from sklearn.neighbors import KNeighborsClassifier <- Remove the classifier | Remover o classificador (Step 1)
# Creating classifier | Criando classificador 
my_classifier = ScrappyKNN() # (Step 2)

# Training the classifier | Treinando o classificador 
my_classifier.fit(X_train, y_train)

# Predictions | Previsões 
predictions = my_classifier.predict(X_test, y_test)

# Accuracy | Precisão : (Step 8)
from sklearn.metrics import accuracy_score
print(f'Accuracy Score of ScrappyKNN: {accuracy_score(y_test, predictions)}')