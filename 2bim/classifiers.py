import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# carrega dados do arquivo csv
data = pd.read_csv('diabetes.csv', encoding='utf-8', delimiter=',',usecols=['Pregnancies', 'Glucose', 'BloodPressure', 
                                                                            'SkinThickness', 'Insulin', 'BMI', 
                                                                          'DiabetesPedigreeFunction', 'Age','Outcome'])

print(data.head())

# separa as variáveis preditoras do desfecho
y = data['Outcome']
# todas as colunas, exceto a Outcome e grava em x
X = data.drop('Outcome', axis = 1)

# test_size 30% 0.3 30% dos valores foram utilizados para teste 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) 

model1 = LogisticRegression()
model1.fit(X_train, y_train)

model2 = RandomForestClassifier()
model2.fit(X_train, y_train)

model3 = KNeighborsClassifier()
model3.fit(X_train, y_train)


# avalia o modelo de acordo com os dados de teste
yhat1 = model1.predict(X_test)
yhat2 = model2.predict(X_test)
yhat3 = model3.predict(X_test)


# avalia a precisão comparando o modelo criado yhat, 
# com o conjunto de dados de teste y_test
accuracy1 = accuracy_score(y_test, yhat1)
print('Accuracy LogisticRegression: %.2f' % (accuracy1*100))

accuracy2 = accuracy_score(y_test, yhat2)
print('Accuracy RandomForestClassifier: %.2f' % (accuracy2*100))

accuracy3 = accuracy_score(y_test, yhat3)
print('Accuracy KNeighborsClassifier: %.2f' % (accuracy3*100))

