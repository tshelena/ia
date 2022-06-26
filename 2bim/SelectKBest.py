# rankeamento dos atributos, conforme pontuação do SelectkBest
# tinha escolhido retirar o SkinThickness antes de testar
# dessa forma. resolvi testar para ver se tinha ficado
# muito fora do esperado, e então refazer se fosse o caso
# não refiz pq ficou bem semelhante, mas deixei aqui o código
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
from matplotlib import pyplot

# carregando o conjunto de dados
def load_dataset(filename):
# carregando o conjunto de dados no DataFrame
    data = read_csv(filename, header=None)
    dataset = data.values
# dividindo variáveis de entrada e saída / preditoras (X) e desfecho (Y)
    X = dataset[:, :-1]
    y = dataset[:,-1]
    return X, y

# selecionando os recursos
def select_features(X_train, y_train, X_test):
# configurando para selecionar todos os atributos
    fs = SelectKBest(score_func=f_classif, k='all')
# treinando os dados selecionados
    fs.fit(X_train, y_train)
# treinando os dados de entrada
    X_train_fs = fs.transform(X_train)
# testando os dados de entrada
    X_test_fs = fs.transform(X_test)
    return X_train_fs, X_test_fs, fs
# carregando o banco de dados
X, y = load_dataset('diabetes.csv')
# separando em dados de treino e dados de teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)
# selecionando os dados de treinamento e teste do atributos
X_train_fs, X_test_fs, fs = select_features(X_train, y_train, X_test)
# calculando a pontuação de cada atributo
for i in range(len(fs.scores_)):
    print('Atributo %d: %f' % (i, fs.scores_[i]))
# plot das pontuações
pyplot.bar([i for i in range(len(fs.scores_))], fs.scores_)
pyplot.show()

#Atributo 0: 21.952926
#Atributo 1: 134.995132
#Atributo 2: 1.868609 'BloodPressure',                                                                         
#Atributo 3: 2.141532 'SkinThickness'
#Atributo 4: 6.303769
#Atributo 5: 41.691993
#Atributo 6: 11.759834
#Atributo 7: 26.831139