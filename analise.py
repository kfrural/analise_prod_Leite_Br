# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Carregando os dados
df = pd.read_csv('producao_leite.csv')

# Explorando os dados
print(df.head())
print(df.info())

# Visualizando a produção de leite por região
plt.figure(figsize=(10, 6))
sns.barplot(x='regiao', y='producao', data=df)
plt.title('Produção de Leite por Região')
plt.xlabel('Região')
plt.ylabel('Produção (litros)')
plt.show()

# Visualizando a produção de leite por ano e por região
plt.figure(figsize=(12, 8))
sns.barplot(x='ano', y='producao', hue='regiao', data=df)
plt.title('Produção de Leite por Ano e por Região')
plt.xlabel('Ano')
plt.ylabel('Produção (litros)')
plt.legend(title='Região')
plt.show()

# Analisando a relação entre produção e tecnologia
plt.figure(figsize=(10, 6))
sns.scatterplot(x='ano', y='producao', data=df)
plt.title('Relação entre Produção e Ano')
plt.xlabel('Ano')
plt.ylabel('Produção (litros)')
plt.show()

# Modelando a produção de leite
X = df[['tecnologia', 'genetica', 'manejo']]
y = df['producao']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print('Coeficientes:', model.coef_)
print('Intercepto:', model.intercept_)

y_pred = model.predict(X_test)
mse = np.mean((y_test - y_pred)**2)
print('MSE:', mse)

# Fazendo previsões
new_data = pd.DataFrame({'tecnologia': [80], 'genetica': [90], 'manejo': [85]})
predicted_production = model.predict(new_data)
print('Produção Prevista:', predicted_production[0])


